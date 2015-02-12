# -!- encoding: utf-8 -!-

import fileinput
import sys
import csv

writer = csv.DictWriter(sys.stdout, ['Date', 'Payee', 'Category', 'Memo', 'Outflow', 'Inflow'])
writer.writeheader()


class input_csv_dialect(csv.excel):
    delimiter = ';'
    

contents = fileinput.input()
reader = csv.DictReader(contents, ['Számlaszám', 'T(erhelés)/J(óváírás)', 'Összeg', 'Pénznem', 'Könyvelési dátum', 'Értéknap',
                          'Új könyvelt egyenleg', 'Ellenoldali számlaszám', 'Ellenoldali név', 'Közlemény', 'Közlemény 2',
                          'Közlemény 3', 'Forgalom típusa'], dialect=input_csv_dialect)


def date(r):
    field = r['Könyvelési dátum']
    return '%s/%s/%s' % (field[:4], field[4:6], field[6:8])


def strip_paypass(s):
    if s.endswith('PPASS'):
        return s[:-5]
    return s


def payee(r):
    if r['Forgalom típusa'] == 'VÁSÁRLÁS KÁRTYÁVAL':
        return strip_paypass(r['Közlemény'])
    if r['Közlemény'] == 'VÁSÁRLÁS KÁRTYÁVAL':  # Credit card
        return strip_paypass(r['Közlemény 2'])
    if r['Forgalom típusa'] in ['KP.FELVÉT/-BEFIZ. DÍJA', 'ESETI MEGBÍZÁSOK KÖLTSÉGE', 'OTPdirekt ÜZENETDÍJ']:
        return 'OTP'
    if r['Forgalom típusa'] == 'KÉSZPÉNZFELVÉT ATM-BŐL':
        return 'KÉSZPÉNZFELVÉT ATM-BŐL'
    return '%s %s' % (r['Ellenoldali számlaszám'],
                      r['Ellenoldali név'])


def category(r):
    return ''
    

def memo(r):
    if r['Közlemény'] == 'VÁSÁRLÁS KÁRTYÁVAL':  # Credit card
        return r['Közlemény 3']
    return ('%s %s %s' % (r['Közlemény'], r['Közlemény 2'], r['Közlemény 3'])).strip() or r['Forgalom típusa']


def outflow(r):
    x = int(r['Összeg'])
    if x < 0:
        assert r['T(erhelés)/J(óváírás)'] == 'T'
        return -x
    return 0

    
def inflow(r):
    x = int(r['Összeg'])
    if x > 0:
        assert r['T(erhelés)/J(óváírás)'] == 'J'
        return x
    return 0
    

for record in reader:
    data = {
        'Date': date(record).strip(),
        'Payee': payee(record).strip(),
        'Category': category(record).strip(),
        'Memo': memo(record).strip(),
        'Outflow': outflow(record),
        'Inflow': inflow(record)
    }
    writer.writerow(data)

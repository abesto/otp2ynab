# otp2ynab

Converts OTP expense report CSVs to YNAB4 importable CSVs. Uses python2.

[OTP](https://www.otpbank.hu) is a Hungarian bank.

[YNAB4](http://www.youneedabudget.com/) is a personal budgeting tool.

## Usage

Download ("Export") a CSV expense report from OTP Direkt (the online interface), then:

```sh
python main.py ~/Downloads/export.csv > out.csv
```

Then import `out.csv` into YNAB. Make sure to select the right account before importing.
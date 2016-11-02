# otp2ynab

Converts OTP expense report XMLs to nYNAB importable OFXs using `ofxstatement`.

[OTP](https://www.otpbank.hu) is a Hungarian bank.

[YNAB4](http://www.youneedabudget.com/) is a personal budgeting tool.

## Requirements

 * python3
 * virtualenv

## Usage

Download ("Export") an XML expense report from OTP Direkt (the online interface), then:

```sh
./convert.sh ~/Downloads/export.xml
```

Then import `out.csv` into YNAB. Make sure to select the right account before importing.

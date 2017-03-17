# edtProject
"edt" stand for "emplois du temps" which mean timetable in french

Why bother to log yourself in a website if a python script can send you an sms with all the data you need :p

# how to test it ?

First you have to clone the repo.

Then make a copy of sms-example.py and name it sms.py.
Fill those four variables by creating an account on twilio.com:

```python
accountSID = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
authToken = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
myTwilioNumber = '+33122334455'
myCellPhone = '+33118218072' #don't call :p (this is a random number)
```

You might need to install the twilio API as well: `pip install twilio`

And in edt.py you may want to change the url who target my icalendar to yours.

Then run `python3 /path/to/the/repo/main.py`
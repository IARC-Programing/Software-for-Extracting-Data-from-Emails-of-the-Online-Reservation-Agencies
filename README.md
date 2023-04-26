# Software for Extracting Data from Emails of the Online Reservation Agencies

---

- Original By [Mesa Charoenwai](https://github.com/6210110291)
- Advisor Assoc.Prof. Dr. Pichaya Tandayya

## Abstract

The software for extracting data from emails of the online reservation agencies. It is a system that helps handling hotel reservation emails. This software system will extract important information from the booking confirmation emails in Gmail. First, it checks whether it is a booking confirmation email or not. Next, this extracted information will be sent to the hotel software system for automatic booking or other purposes. Important information includes booking name, booking time, number of guests, dates of stay, number of days, and other additional details.

## Development

- Create Virtual Environment

```
python -m venv venv
```

- Install Dependencies

```
pip install -r requirement.txt
```

- Create `credentails.json` file like in `credential.example.json` and get them from Google Cloud Platform

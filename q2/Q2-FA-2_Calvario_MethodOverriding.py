class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85


print("Hospital Billing System")
print("                       ")

regular_patient = Patient("Tia Wolfe", 15000)
senior_patient = SeniorPatient("Steven Bilinger", 15000)
philhealth_patient = PhilHealthPatient("Rogers Canton", 15000)

patients = [regular_patient, senior_patient, philhealth_patient]

for patient in patients:
    print(f"Patient Name:  {patient.get_name()}")
    print(f"Original Bill: ₱{patient.get_bill_amount():,.2f}")
    print(f"Final Bill:    ₱{patient.calculate_bill():,.2f}")
    print()
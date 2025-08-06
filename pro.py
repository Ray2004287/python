class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"နာမည်: {self.name}, ဖုန်း: {self.phone}, အီးမေးလ်: {self.email}"


class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.name] = contact
        print("✅ Contact အသစ်ထည့်ပြီးပါပြီ။")

    def view_contact(self, name):
        contact = self.contacts.get(name)
        if contact:
            print(contact)
        else:
            print("❌ ဒီနာမည်နဲ့ contact မရှိပါ။")

    def edit_contact(self, name, new_phone, new_email):
        if name in self.contacts:
            self.contacts[name].phone = new_phone
            self.contacts[name].email = new_email
            print("✅ Contact ပြင်ပြီးပါပြီ။")
        else:
            print("❌ Contact မတွေ့ပါ။")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("🗑️ Contact ဖျက်ပြီးပါပြီ။")
        else:
            print("❌ Contact မတွေ့ပါ။")

    def show_all_contacts(self):
        if not self.contacts:
            print("📭 Contact မရှိသေးပါ။")
        else:
            for contact in self.contacts.values():
                print(contact)

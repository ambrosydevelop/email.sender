from get_items import GetItems
from send_email import send_email
import eel


eel.init('web')

def main(message,subject,file) -> None:
    """Get accounts and send email"""
    count = 0

    for user in GetItems.get_user_account(): #Your accounts
        for email in GetItems.get_adress(): #Get email of attack users
            send_email(
                message, 
                subject,
                user[0],
                user[1],
                email,
                file
            )
            count += 1
            eel.python_call(str(count)) #Cycle output

if __name__ == '__main__':
    @eel.expose
    def on_click_js(x):
        main(x['message'],x['subject'],x['file'])
eel.start('index.html',size=(300,300))
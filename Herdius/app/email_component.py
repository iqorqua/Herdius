import threading
import gmail
import uuid
from app.models import RegistrationRequest, ChangePasswordRequest

html = """\
<table border="1" style="border-collapse: collapse; width: 100%;">
<tbody>
<tr style="height: 125px; background-color: gray;">
<td style="width: 892px; height: 125px;">
<h1 style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #4485b8;"><img src="http://www.opnplatform.io/static/app/img/logo.png" alt="icon" width="242" height="65" style="display: block; margin-left: auto; margin-right: auto;" /></h1>
<h1 style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #4485b8; text-align: center;"><span style="color: #ffffff;">Herdius ICO r<span style="font-family: inherit;">egistration!</span></span></h1>
</td>
</tr>
</tbody>
</table>
<h4><span style="color: #000000;">This email was selected as main address. If you are owner and you had <strong>NO</strong> attemptions to registrate in ICO system, please, delete this message!</span></h4>
<p><span style="color: #000000;"></span></p>
<h4>To finish registration, use this link:</h4>
<p style="text-align: center;"><a href="myhref">Finish registration</a></p>
<p></p>
<p></p>
<hr />
<p style="text-align: right;"><em>Best reguards</em></p>
<p style="text-align: right;"><em>Herdius ICO Team</em></p>
"""
html1 = """\
<table border="1" style="border-collapse: collapse; width: 100%;">
<tbody>
<tr style="height: 125px; background-color: gray;">
<td style="width: 892px; height: 125px;">
<h1 style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #4485b8;"><img src="http://www.opnplatform.io/static/app/img/logo.png" alt="icon" width="242" height="65" style="display: block; margin-left: auto; margin-right: auto;" /></h1>
<h1 style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #4485b8; text-align: center;"><span style="color: #ffffff;">Herdius ICO p<span style="font-family: inherit;">assword recovery!</span></span></h1>
</td>
</tr>
</tbody>
</table>
<h4><span style="color: #000000;"></span></h4>
<p><span style="color: #000000;"></span></p>
<h4>To change password, use this link:</h4>
<p style="text-align: center;"><a href="myhref">Change password</a></p>
<p></p>
<p></p>
<hr />
<p style="text-align: right;"><em>Best reguards</em></p>
<p style="text-align: right;"><em>Herdius ICO Team</em></p>
"""

def send_email_async(user):
    my_thread = threading.Thread(target=_send_email, args=(user,))
    my_thread.start()

def send_email_pass_change_req_async(user):
    my_thread = threading.Thread(target=_send_email_passchange, args=(user, ))
    my_thread.start()
    
def _send_email(user):
     registration_uuid = uuid.uuid4()
     RegistrationRequest.objects.create(user_pk=user.pk, user_registration_uuid = registration_uuid)
     g = gmail.GMail('lilb0w33p@gmail.com', '123456789qQ')
     msg = gmail.Message('Herdius ICO Registration', to = user.email, html=html.replace('myhref', 'http://www.opnplatform.io/development/activate/' + str(registration_uuid)))
     g.send(msg)
    
def _send_email_passchange(user):
     registration_uuid = str(uuid.uuid4())
     registration_uuid = registration_uuid + str(uuid.uuid4())
     ChangePasswordRequest.objects.create(user_pk=user.pk, user_token = registration_uuid)
     g = gmail.GMail('lilb0w33p@gmail.com', '123456789qQ')
     msg = gmail.Message('Herdius ICO Password changing', to = user.email, html=html1.replace('myhref', 'http://www.opnplatform.io/development/changepass/' + str(registration_uuid)))
     g.send(msg)

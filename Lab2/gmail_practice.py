# from gmail import GMail, Message
# import random
#
# gmail_template = ["""Hi Mr.Huy,
#
# Em xin phép được nghỉ buổi học hôm nay vì lý do kỉ niệm 1 tuần với gấu ạ hí hí :3
#
# Em cảm ơn anh đzai ^^""", """Hi Mr.Huy,
#
# Em xin phép được nghỉ buổi học hôm nay vì em đang bị cảm nắng 1 bạn cùng lớp ạ hí hí :3
#
# Em cảm ơn anh đzai ^^""", """Hi Mr.Huy,
#
# Em xin phép được nghỉ buổi học hôm nay vì tim em vừa bị 1 bạn gái đánh cắp mất ạ hic hic :(
#
# Em cảm ơn anh đzai ^^""", """<p>Hi Mr.Huy đẹp trai,</p>
# <p>Anh c&oacute; biết rằng <strong>m&ugrave;a đ&ocirc;ng</strong> sắp đến rồi kh&ocirc;ng? Vậy m&agrave; em vẫn chưa c&oacute; gấu, m&agrave; em mới xem dự b&aacute;o thời tiết ng&agrave;y mai trời sẽ m&aacute;t n&ecirc;n em muốn xin ph&eacute;p anh cho em nghỉ buổi học ng&agrave;y mai để đi kiếm gấu ạ :3 aihihi ^^</p>
# <p>Hi vọng anh sẽ đồng &yacute;, v&igrave; 1 tương lai kh&ocirc;ng c&ocirc; đơn của em ạ :p</p>
# <p>Em cảm ơn anh rất nh&igrave;u ^!&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-embarassed.gif" alt="embarassed" /></p>
# <p><img src="https://www.google.com.vn/url?sa=i&amp;rct=j&amp;q=&amp;esrc=s&amp;source=images&amp;cd=&amp;cad=rja&amp;uact=8&amp;ved=0ahUKEwiAzfiH1MXXAhUBErwKHbY2AqEQjRwIBw&amp;url=http%3A%2F%2Fwww.fanpop.com%2Fclubs%2Fbeing-nice%2Fimages%2F133524%2Ftitle%2Fbear-hugs-4-u-photo&amp;psig=AOvVaw3TXVF-eJFwf0VsAycvkipT&amp;ust=1511009732076884" alt=":3" width="100" height="100" /></p>
#
# """]
#
# gmail = GMail('c4e13.lab.long@gmail.com','lov3lov3')
#
# msg = Message('Hello',to='c4e13.lab.huynq@gmail.com',html=random.choice(gmail_template))
#
# gmail.send(msg)


from gmail import GMail, Message
from random import choice

# Select random file
file_names = ['1.html', '2.html', '3.html']
file_name = choice(file_names)

# Select random reason
reasons = ['tim em vừa bị 1 bạn g&aacute;i đ&aacute;nh cắp mất ạ hic hic :(', 'l&yacute; do kỉ niệm 1 tuần với gấu ạ h&iacute; h&iacute; :3', 'em đang bị cảm nắng 1 bạn c&ugrave;ng lớp ạ h&iacute; h&iacute; :3']
reason = choice(reasons)

# read html-content
template_file = open(file_name, encoding = 'utf-8')
html_content = template_file.read()
template_file.close()

# Render reason
html_content = html_content.replace('{{reason}}', reason)

# Send it
gmail = GMail('c4e13.lab.long@gmail.com','lov3lov3')

msg = Message('Hello',to='c4e13.lab.huynq@gmail.com',html=html_content)

gmail.send(msg)

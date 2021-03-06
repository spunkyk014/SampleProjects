from .models import URLEntry

def UniqueID(url, user):
    #expects that url is a string and user is a User object
    cleaned_url = url.replace("http://", "")
    cleaned_url = cleaned_url.replace("www", "")
    cleaned_url = cleaned_url.replace("/", "")
    cleaned_url = cleaned_url.replace(".", "")
    url_len = len(cleaned_url)
    num_digits = (url_len % 5) + 1
    interval = len(cleaned_url)/num_digits
    index = 0
    id = ""
    for x in range(0,num_digits):
        if index < len(cleaned_url):
            id += cleaned_url[index]
            index += interval


    is_duplicate = False
    previous_url_entry = URLEntry.objects.filter(url_id=id)
    if previous_url_entry.exists():
        if previous_url_entry[0].user == user  and  previous_url_entry[0].original_url == url:
            is_duplicate = True
        else:
            id = ((url_len + 1)*len(id))%10000
            previous_url_entry = URLEntry.objects.filter(url_id=id)
            while previous_url_entry.exists()  and  len(str(id))<6:
                if previous_url_entry[0].user == user and previous_url_entry[0].original_url == url:
                    is_duplicate = True
                    break
                else:
                    id += 1
                    previous_url_entry = URLEntry.objects.filter(url_id=id)

    if URLEntry.objects.filter(url_id=id).exists()  and  not is_duplicate:
        #if for some reason we end up here, which we probably won't, the empty string means we couldn't find a place for it
        id = ""

    return str(id), is_duplicate

def CreateShortenedURL(username, id):
    return str("remishakes.herokuapp.com/kg." + str(username) + "." + str(id) + "/")
    # url(r'^host_site/(?P<user_id>\w+\d*).(?P<pk>\w{1,10})$', views.URLRedirect, name='url_redirect'),


def IsUserLoggedIn(request, username):
    return request.user.username == username

from models import User, Day, Course

def query_data(user):
    print("hi")
    # current_user = User.objects.get(name = user)
    # friend_list = list(current_user.friend_set.all())

    # return friend_list


if __name__ == '__main__':
    print(query_data("TestUser"))


# This entire file will be ignored by Pylint. pylint: skip-file

"""
1. მომხმარებლის კლასი:

- ინიციალიზდება მომხმარებლის სახელით, ცარიელი ლისტით პოსტებისთვის და ცარიელი სეტით მეგობრებისთვის.

- მეთოდები მოიცავს პოსტის შექმნას, პოსტის კომენტარებს, პოსტის მოწონებას.


2. პოსტის კლასი :

- ინიციალიზებულია შინაარსით, ავტორით, კომენტარების სიით, მოწონებების სიით

- მეთოდები მოიცავს კომენტარის დამატებას და მოწონების დამატებას.


3. კომენტარების კლასი:

- ინიციალიზებულია შინაარსით და ავტორით.


4. გამოყენება:

- ქმნის ორ მომხმარებელს, ამეგობრებს მათ.

- User1 ქმნის პოსტს, User2 კომენტარს აკეთებს მასზე და User1 ალაიქებს კომენტარს.

- User1 ქმნის სხვა პოსტს და User2 ალაიქებს.
"""


class User:
    def __init__(self, username):
        self.username = username
        self.posts = []
        self.friends = set()

    def add_friend(self, friend):
        if friend != self and friend not in self.friends:
            self.friends.add(friend)
            friend.friends.add(self)
            print(f"{self.username} და {friend.username} დამეგობრდნენ.")
        else:
            print("დამეგობრება ვერ მოხერხდა.")

    def create_post(self, content):
        if content.strip():
            post = Post(content, self)
            self.posts.append(post)
            print(f"{self.username}-მ შექმნა პოსტი: '{content}'")
            return post
        else:
            print("ცარიელი პოსტის შექმნა არ შეიძლება.")
            return None

    def like_post(self, post):
        if self not in post.likes:
            post.likes.add(self)
            print(f"{self.username}-მ მოიწონა პოსტი: '{post.content}'")
        else:
            print(f"{self.username}-მ უკვე მოიწონა ეს პოსტი.")

    def get_comments(self, post):
        return post.comments


class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.comments = []
        self.likes = set()

    def add_comment(self, user, comment_text):
        comment = Comment(comment_text, user)
        self.comments.append(comment)
        print(f"{user.username}-მ დააკომენტარა პოსტზე '{self.content}': {comment_text}")
        return comment

    def add_like_comment(self, user, comment):
        if user not in comment.likes:
            comment.likes.add(user)
            print(
                f"{user.username}-მა მოიწონა {comment.author.username}-ის კომენტარი '{comment.content}' "
            )
        else:
            print(f"{user.username}-მ უკვე მოიწონა ეს კომენტარი.")


class Comment:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.likes = set()


user1 = User("user1")
user2 = User("user2")

user1.add_friend(user2)


post1 = user1.create_post("პირველი პოსტი")

comment1 = post1.add_comment(user2, "კარგია")

post1.add_like_comment(user1, comment1)


post1 = user1.create_post("მეორე პოსტი")

user2.like_post(post1)

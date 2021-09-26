from apps.users.handler import user_handler

class TestUser:
    def test_user_class(x):
        event = "Herer"
        user_handler(event, None)
        x = 1 + 1
        assert (x == 2)


if __name__ == '__main__':
    test = TestUser()
    test.test_user_class()

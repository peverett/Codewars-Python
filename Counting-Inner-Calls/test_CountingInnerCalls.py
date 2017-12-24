from CountingInnerCalls import count_calls

def add(a, b):
  return a + b
  

def add_ten(a):
  return add(a, 10)


def misc_fun():
  return add(add_ten(3), add_ten(9))

class TestCountingInnerCalls(object):

    def test_add(self):
        assert count_calls(add, 8, 12) == (0, 20)

    def test_add_ten(self):
        assert count_calls(add_ten, 5) == (1, 15)

    def test_misc_fun(self):
        assert count_calls(misc_fun) == (5, 32)

#test.assert_equals(count_calls(add, 8, 12), (0, 20))
#test.assert_equals(count_calls(add_ten, 5), (1, 15))
#test.assert_equals(count_calls(misc_fun), (5, 32))

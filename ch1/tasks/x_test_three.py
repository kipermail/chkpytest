"""Проверим тип данных Task."""
import pytest

from collections import namedtuple
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_defaults():
    """Без использования параметров, следует ссылаться на значения по умолчанию."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

#@pytest.mark.run_these_please
def test_member_access():
    """Проверка свойства .field (поля) namedtuple."""
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)

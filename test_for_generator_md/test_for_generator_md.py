import unittest
from generate_md_with_terminal import Connect
class TestTask(unittest.TestCase):
    def test_get_md_link(self):
        example = Task('Merge Intervals', 'https://leetcode.com/problems/merge-intervals/', '    print(a)')
        expect = '+ [Merge Intervals](#merge-intervals)'
        result = example.get_md_link()
        self.assertEqual(expect, result)
    def test_get_md_title(self):
        example = Task('Merge Intervals', 'https://leetcode.com/problems/merge-intervals/', '    print(a)')
        expect = '## Merge Intervals'
        result = example.get_md_title()
        self.assertEqual(expect, result)
    def test_get_md_python_solution(self):
        example = Task('Merge Intervals', 'https://leetcode.com/problems/merge-intervals/', '    print(a)')
        expect = '``` python\n\n```'
        result = example.get_md_python_solution()
        self.assertEqual(expect, result)
    def test_get_md_task_content(self):
        example = Task('Merge Intervals', 'https://leetcode.com/problems/merge-intervals/', '    1')
        expect = ('+ [Merge Intervals](#merge-intervals)', '## Merge Intervals\n\nhttps://leetcode.com/problems/merge-intervals/\n\n``` python\n\n```')
        result = example.get_md_task_content()
        self.assertEqual(expect, result)
if __name__ == '__main__':
    unittest.main()

import sys

LINK_SOLUTION_SEPARATE = '<---end.markdown links--->'
def get_all_lines_from_file(file_name):
    file=open(file_name)
    syp = file.readlines()
    return syp
def get_file_content(file_name):
    file = open(file_name)
    src = file.read()
    file.close
    return  src
def write_to_md_file(file_name, md_solution):
    file = open(file_name, "w")
    file.write(md_solution)
    file.close
def merge_solution(old_md_links, old_solution, new_md_link, new_solution):
    return "{}\n{}{}{}\n{}".format(old_md_links,new_md_link,LINK_SOLUTION_SEPARATE,old_solution,new_solution)
def str(self):
    return '{}\n{}\n{}'.format(self.title,self.link,self.sourse_code)
class Connect:
    def __init__(self, title, link, sourse_code):
        self.title = title.split('. ')[-1].strip('\n')
        self.link = link.strip('\n')
        self.sourse_code = sourse_code
    def get_md_link(self):
        return '+ [{}](#{})'.format(self.title, self.link[30:(len(self.link)-1)])
    def get_md_title(self):
        return '## {}'.format(self.title)
    def get_md_python_solution(self):
        return '``` python\n{}\n```'.format(
            ''.join(map(lambda x: x[4:], self.sourse_code)))
    def get_md_task_content(self):
        return self.get_md_link(), '{}\n\n{}\n\n{}'.format(self.get_md_title(), self.link, self.get_md_python_solution())

def main(a,b):
    sourse_lines = get_all_lines_from_file(a)
    task = Task(sourse_lines[0], sourse_lines[1], sourse_lines[3:])
    new_md_link, new_md_task = task.get_md_task_content()
    old_md_links,old_md_task = get_file_content(b).split("<---end.markdown links--->")
    write_to_md_file(b, merge_solution(old_md_links, old_md_task, new_md_link, new_md_task))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

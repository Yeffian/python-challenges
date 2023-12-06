from datetime import datetime
project_start = datetime.strptime(input('When did the project start? (<Month> <Date> <Year>)'), '%b %d %Y')
project_end = datetime.strptime(input('When did the project end? (<Month> <Date> <Year>)'), '%b %d %Y')
print(abs(project_start - project_end))


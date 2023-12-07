PLANTS = {'C': 'Clover',
        'G': 'Grass',
        'R': 'Radishes',
        'V': 'Violets'}

STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']         

class Garden:
    def __init__(self, diagram, students=STUDENTS):
        self.diagram = diagram
        self.students = students

        
    def plants(self,chosen_students):
        
        starting_index = 0
        for position, student in enumerate(sorted(self.students)):
            if student in chosen_students:
                starting_index = position * 2    

        rows = self.diagram.split('\n')
        student_plants = [r[starting_index:starting_index+2] for r in rows]

        return [PLANTS[p] for sp in student_plants for p in sp]        

garden = Garden("VVCCGG\nVVCCGG")
print(garden.plants("Bob"))      
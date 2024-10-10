class College:
    def __init__(self, name):
        self.name = name

class Staff(College):
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role

# Multiple Inheritance Example
class Assets:
    def __init__(self, asset_name):
        self.asset_name = asset_name

class Admin(Staff, Assets):
    def __init__(self, name, role, asset_name):
        Staff.__init__(self, name, role)
        Assets.__init__(self, asset_name)

# Multilevel Inheritance Example
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

# Hierarchical Inheritance Example
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

class AdminStaff(Employee):
    def __init__(self, name, emp_id, role):
        super().__init__(name, emp_id)
        self.role = role

# Hybrid Inheritance Example (Combination of multiple types)
class Building:
    def __init__(self, building_name):
        self.building_name = building_name

class Faculty(Staff, Building):
    def __init__(self, name, role, building_name):
        Staff.__init__(self, name, role)
        Building.__init__(self, building_name)
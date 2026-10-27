class PisayCampus:
    def __init__(self, campus_director):
        self.__campus_director = campus_director

    @property
    def campus_director(self):
        return self.__campus_director

    @campus_director.setter
    def campus_director(self, value):
        self.__campus_director = value

    def show_institution(self):
        print("Campus: PSHS - Zamboanga Peninsula Region Campus (ZRC)")

    def show_top_official(self):
        print("Campus Director:", self.campus_director)


class CurriculumInstruction(PisayCampus):
    def __init__(self, campus_director, cid_chief, batch_year, total_units):
        super().__init__(campus_director)
        self.__cid_chief = cid_chief
        self.__batch_year = batch_year
        self.__total_units = total_units

    @property
    def cid_chief(self):
        return self.__cid_chief

    @cid_chief.setter
    def cid_chief(self, value):
        self.__cid_chief = value

    @property
    def batch_year(self):
        return self.__batch_year

    @batch_year.setter
    def batch_year(self, value):
        self.__batch_year = value

    @property
    def total_units(self):
        return self.__total_units

    @total_units.setter
    def total_units(self, value):
        self.__total_units = value

    def show_cid_leadership(self):
        print("CID Chief:", self.cid_chief)
        print("Academic Year:", self.batch_year)

    def verify_unit_load(self):
        print("Total Subject Units:", self.total_units)


class StudentServices(PisayCampus):
    def __init__(self, campus_director, ssd_chief, core_program):
        super().__init__(campus_director)
        self.__ssd_chief = ssd_chief
        self.__core_program = core_program

    @property
    def ssd_chief(self):
        return self.__ssd_chief

    @ssd_chief.setter
    def ssd_chief(self, value):
        self.__ssd_chief = value

    @property
    def core_program(self):
        return self.__core_program

    @core_program.setter
    def core_program(self, value):
        self.__core_program = value

    def show_ssd_leadership(self):
        print("SSD Chief:", self.ssd_chief)

    def display_welfare_action(self):
        print("Primary Service:", self.core_program)


class AcademicUnit(CurriculumInstruction):
    def __init__(self, campus_director, cid_chief, batch_year, total_units, stem_discipline):
        super().__init__(campus_director, cid_chief, batch_year, total_units)
        self.__stem_discipline = stem_discipline

    @property
    def stem_discipline(self):
        return self.__stem_discipline

    @stem_discipline.setter
    def stem_discipline(self, value):
        self.__stem_discipline = value

    def show_specialization(self):
        print("STEM Unit Discipline:", self.stem_discipline)


class EvaluationUnit(CurriculumInstruction):
    def __init__(self, campus_director, cid_chief, batch_year, total_units, exam_type):
        super().__init__(campus_director, cid_chief, batch_year, total_units)
        self.__exam_type = exam_type

    @property
    def exam_type(self):
        return self.__exam_type

    @exam_type.setter
    def exam_type(self, value):
        self.__exam_type = value

    def show_assessment_style(self):
        print("Assessment Type:", self.exam_type)


class ScholarExamination(EvaluationUnit):
    def __init__(self, campus_director, cid_chief, batch_year, total_units, exam_type, target_date):
        super().__init__(campus_director, cid_chief, batch_year, total_units, exam_type)
        self.__target_date = target_date

    @property
    def target_date(self):
        return self.__target_date

    @target_date.setter
    def target_date(self, value):
        self.__target_date = value

    def show_exam_block(self):
        print("Exam Administration Date:", self.target_date)


class FacultyDevelopment(CurriculumInstruction):
    def __init__(self, campus_director, cid_chief, batch_year, total_units, training_module):
        super().__init__(campus_director, cid_chief, batch_year, total_units)
        self.__training_module = training_module

    @property
    def training_module(self):
        return self.__training_module

    @training_module.setter
    def training_module(self, value):
        self.__training_module = value

    def show_training_focus(self):
        print("Active Faculty Training:", self.training_module)


class ScholarWelfare(StudentServices):
    def __init__(self, campus_director, ssd_chief, core_program, support_project):
        super().__init__(campus_director, ssd_chief, core_program)
        self.__support_project = support_project

    @property
    def support_project(self):
        return self.__support_project

    @support_project.setter
    def support_project(self, value):
        self.__support_project = value

    def show_welfare_project(self):
        print("Scholar Welfare Support:", self.support_project)


# Instantiate the administrative structure with unique mock records
zrc_campus = PisayCampus("Dir. Gallamaso")
cid_registry = CurriculumInstruction("Dir. Gallamaso", "Chief Raznee", "2026-2027", 8)
ssd_registry = StudentServices("Dir. Gallamaso", "Chief Gamil", "Guidance & Counseling")

science_dept = AcademicUnit("Dir. Gallamaso", "Chief Raznee", "2026-2027", 8, "Natural Sciences")
grading_dept = EvaluationUnit("Dir. Gallamaso", "Chief Raznee", "2026-2027", 8, "Quarterly Exams")
periodic_test = ScholarExamination("Dir. Gallamaso", "Chief Raznee", "2026-2027", 8, "Quarterly Exams", "October 20")
pedagogy_track = FacultyDevelopment("Dir. Gallamaso", "Chief Raznee", "2026-2027", 8, "STEM Teaching Seminars")
wellness_office = ScholarWelfare("Dir. Gallamaso", "Chief Gamil", "Guidance & Counseling", "Mental Health Break Initiatives")

# Execution Blocks
print("=== PISAY EXECUTIVE ADMIN ===")
zrc_campus.show_institution()
zrc_campus.show_top_official()

print("\n=== CURRICULUM & INSTRUCTION DIVISION ===")
cid_registry.show_top_official()
cid_registry.show_cid_leadership()
cid_registry.verify_unit_load()

print("\n=== STUDENT SERVICES DIVISION ===")
ssd_registry.show_top_official()
ssd_registry.show_ssd_leadership()
ssd_registry.display_welfare_action()

print("\n=== CID: ACADEMIC CORE ===")
science_dept.show_cid_leadership()
science_dept.show_specialization()

print("\n=== CID: EVALUATION MODULE ===")
grading_dept.show_cid_leadership()
grading_dept.show_assessment_style()

print("\n=== CID: TESTING CALENDAR ===")
periodic_test.show_assessment_style()
periodic_test.show_exam_block()

print("\n=== CID: FACULTY TRACK ===")
pedagogy_track.show_cid_leadership()
pedagogy_track.show_training_focus()

print("\n=== SSD: SCHOLAR CARE ===")
wellness_office.show_ssd_leadership()
wellness_office.show_welfare_project()

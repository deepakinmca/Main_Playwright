import pytest
class Test_mySisFamily_test006:
    @pytest.mark.regression
    def test_father_test29(self):
        print ("13 Father name is:",'Natarajan Kuppuswamy')
    def test_mother_test30(self):
        print ("14 Mother name is:","Geetha Natarajan")
    @pytest.mark.regression
    def test_sister_test31(self):
        print ("15 Sister name is:","Maithili Natarajan")
    def test_pappaFirst_test32(self):
        print ("16 Elder name is:","Shruthika Ganesh")
    @pytest.mark.regression
    def test_pappaSecond_test33(self):
        print ("17 Younger name is:","Luxitha Ganesh")
    def test_mama_test34(self):
        print ("18 Mama name is:","Ganesh Mohan")
@pytest.mark.skip
class Test_MyFamily_test007(Test_mySisFamily_test006):
    @pytest.mark.regression
    def test_spouse_test35(self):
        print("19 Spouse name is:","Nandhini Murugesan")
    @pytest.mark.critical
    def test_myself_test36(self):
        print("20 My name is:","Deepak Natarajan")
    @pytest.mark.regression
    def test_kidFirst_test37(self):
        print("21 Innocent name is:","Harshitha Deepak")
    @pytest.mark.critical
    def test_KidSecond_test38(self):
        print("22 Rowdy name is:","Anisha Deepak")
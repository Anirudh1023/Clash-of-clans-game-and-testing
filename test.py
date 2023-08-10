import unittest
from king import King
from points import config_level_1 as config
import village

class TestMove(unittest.TestCase):
    def setUp1(self):
        self.hero = King([17, 35])
        self.village = village.createVillage(1)

    def test_up1(self):
        self.setUp1()
        self.hero.move('up', self.village)
        self.assertEqual(self.hero.position, [16, 35], "incorrect value")

    def test_down1(self):
        self.setUp1()
        self.hero.move('down', self.village)
        self.assertEqual(self.hero.position, [17, 35], "incorrect value")

    def test_left1(self):
        self.setUp1()
        self.hero.move('left', self.village)
        self.assertEqual(self.hero.position, [17, 34], "incorrect value")

    def test_right1(self):
        self.setUp1()
        self.hero.move('right', self.village)
        self.assertEqual(self.hero.position, [17, 35], "incorrect value")

    def setUp2(self):
        self.hero = King([0, 0])
        self.village = village.createVillage(1)

    def test_up2(self):
        self.setUp2()
        self.hero.move('up', self.village)
        self.assertEqual(self.hero.position, [0, 0], "incorrect value")

    def test_down2(self):
        self.setUp2()
        self.hero.move('down', self.village)
        self.assertEqual(self.hero.position, [1, 0], "incorrect value")

    def test_left2(self):
        self.setUp2()
        self.hero.move('left', self.village)
        self.assertEqual(self.hero.position, [0, 0], "incorrect value")

    def test_right2(self):
        self.setUp2()
        self.hero.move('right', self.village)
        self.assertEqual(self.hero.position, [0, 1], "incorrect value")

    def setUp3(self):
        self.hero = King([17, 28])
        self.village = village.createVillage(1)

    def test_up3(self):
        self.setUp3()
        self.hero.move('up', self.village)
        self.assertEqual(self.hero.position, [16, 28], "incorrect value")

    def test_down3(self):
        self.setUp3()
        self.hero.move('down', self.village)
        self.assertEqual(self.hero.position, [17, 28], "incorrect value")

    def test_left3(self):
        self.setUp3()
        self.hero.move('left', self.village)
        self.assertEqual(self.hero.position, [17, 28], "incorrect value")

    def test_right3(self):
        self.setUp3()
        self.hero.move('right', self.village)
        self.assertEqual(self.hero.position, [17, 29], "incorrect value")

    def setUp4(self):
        self.hero = King([17, 26])
        self.village = village.createVillage(1)

    def test_up4(self):
        self.setUp4()
        self.hero.move('up', self.village)
        self.assertEqual(self.hero.position, [16, 26], "incorrect value")

    def test_down4(self):
        self.setUp4()
        self.hero.move('down', self.village)
        self.assertEqual(self.hero.position, [17, 26], "incorrect value")

    def test_left4(self):
        self.setUp4()
        self.hero.move('left', self.village)
        self.assertEqual(self.hero.position, [17, 25], "incorrect value")

    def test_right4(self):
        self.setUp4()
        self.hero.move('right', self.village)
        self.assertEqual(self.hero.position, [17, 26], "incorrect value")

    def setUp5(self):
        self.hero = King([6, 27])
        self.village = village.createVillage(1)

    def test_up5(self):
        self.setUp5()
        self.hero.move('up', self.village)
        self.assertEqual(self.hero.position, [5, 27], "incorrect value")

    def test_down5(self):
        self.setUp5()
        self.hero.move('down', self.village)
        self.assertEqual(self.hero.position, [6, 27], "incorrect value")

    def test_left5(self):
        self.setUp5()
        self.hero.move('left', self.village)
        self.assertEqual(self.hero.position, [6, 27], "incorrect value")

    def test_right5(self):
        self.setUp5()
        self.hero.move('right', self.village)
        self.assertEqual(self.hero.position, [6, 28], "incorrect value")

    def setUp6(self):
        self.hero = King([8, 27])
        self.village = village.createVillage(1)

    def test_up6(self):
        self.setUp6()
        self.hero.move('up', self.village)
        self.assertEqual(self.hero.position, [8, 27], "incorrect value")

    def test_down6(self):
        self.setUp6()
        self.hero.move('down', self.village)
        self.assertEqual(self.hero.position, [9, 27], "incorrect value")

    def test_left6(self):
        self.setUp6()
        self.hero.move('left', self.village)
        self.assertEqual(self.hero.position, [8, 27], "incorrect value")

    def test_right6(self):
        self.setUp6()
        self.hero.move('right', self.village)
        self.assertEqual(self.hero.position, [8, 28], "incorrect value")

    def setUp7(self):
        self.hero = King([16, 14])
        self.village = village.createVillage(1)

    def test_up7(self):
        self.setUp7()
        self.hero.move('up', self.village)
        self.assertEqual(self.hero.position, [16, 14], "incorrect value")

    def test_down7(self):
        self.setUp7()
        self.hero.move('down', self.village)
        self.assertEqual(self.hero.position, [17, 14], "incorrect value")

    def test_left7(self):
        self.setUp7()
        self.hero.move('left', self.village)
        self.assertEqual(self.hero.position, [16, 13], "incorrect value")

    def test_right7(self):
        self.setUp7()
        self.hero.move('right', self.village)
        self.assertEqual(self.hero.position, [16, 14], "incorrect value")

    def setUp8(self):
        self.hero = King([6, 13])
        self.village = village.createVillage(1)

    def test_up8(self):
        self.setUp8()
        self.hero.move('up', self.village)
        self.assertEqual(self.hero.position, [5, 13], "incorrect value")

    def test_down8(self):
        self.setUp8()
        self.hero.move('down', self.village)
        self.assertEqual(self.hero.position, [7, 13], "incorrect value")

    def test_left8(self):
        self.setUp8()
        self.hero.move('left', self.village)
        self.assertEqual(self.hero.position, [6, 13], "incorrect value")

    def test_right8(self):
        self.setUp8()
        self.hero.move('right', self.village)
        self.assertEqual(self.hero.position, [6, 14], "incorrect value")

    def setUp9(self):
        self.hero = King([9, 4])
        self.village = village.createVillage(1)

    def test_up9(self):
        self.setUp9()
        self.hero.move('up', self.village)
        self.assertEqual(self.hero.position, [8, 4], "incorrect value")

    def test_down9(self):
        self.setUp9()
        self.hero.move('down', self.village)
        self.assertEqual(self.hero.position, [9, 4], "incorrect value")

    def test_left9(self):
        self.setUp9()
        self.hero.move('left', self.village)
        self.assertEqual(self.hero.position, [9, 3], "incorrect value")

    def test_right9(self):
        self.setUp9()
        self.hero.move('right', self.village)
        self.assertEqual(self.hero.position, [9, 5], "incorrect value")

    def setUp10(self):
        self.hero = King([8, 30])
        self.village = village.createVillage(1)

    def test_up10(self):
        self.setUp10()
        self.hero.move('up', self.village)
        self.assertEqual(self.hero.position, [8, 30], "incorrect value")

    def test_down10(self):
        self.setUp10()
        self.hero.move('down', self.village)
        self.assertEqual(self.hero.position, [9, 30], "incorrect value")

    def test_left10(self):
        self.setUp10()
        self.hero.move('left', self.village)
        self.assertEqual(self.hero.position, [8, 29], "incorrect value")

    def test_right10(self):
        self.setUp10()
        self.hero.move('right', self.village)
        self.assertEqual(self.hero.position, [8, 31], "incorrect value")

    def setUp11(self):
        self.hero = King([12, 12])
        self.village = village.createVillage(1)

    def test_up11(self):
        self.setUp11()
        self.hero.move('up', self.village)
        self.assertEqual(self.hero.position, [11, 12], "incorrect value")

    def test_down11(self):
        self.setUp11()
        self.hero.move('down', self.village)
        self.assertEqual(self.hero.position, [13, 12], "incorrect value")

    def test_left11(self):
        self.setUp11()
        self.hero.move('left', self.village)
        self.assertEqual(self.hero.position, [12, 11], "incorrect value")

    def test_right11(self):
        self.setUp11()
        self.hero.move('right', self.village)
        self.assertEqual(self.hero.position, [12, 12], "incorrect value")

    def setUp12(self):
        self.hero = King([11, 13])
        self.village = village.createVillage(1)

    def test_up12(self):
        self.setUp12()
        self.hero.move('up', self.village)
        self.assertEqual(self.hero.position, [10, 13], "incorrect value")

    def test_down12(self):
        self.setUp12()
        self.hero.move('down', self.village)
        self.assertEqual(self.hero.position, [11, 13], "incorrect value")

    def test_left12(self):
        self.setUp12()
        self.hero.move('left', self.village)
        self.assertEqual(self.hero.position, [11, 12], "incorrect value")

    def test_right12(self):
        self.setUp12()
        self.hero.move('right', self.village)
        self.assertEqual(self.hero.position, [11, 14], "incorrect value")

    def setUp13(self):
        self.hero = King([11, 24])
        self.village = village.createVillage(1)

    def test_up13(self):
        self.setUp13()
        self.hero.move('up', self.village)
        self.assertEqual(self.hero.position, [10, 24], "incorrect value")

    def test_down13(self):
        self.setUp13()
        self.hero.move('down', self.village)
        self.assertEqual(self.hero.position, [12, 24], "incorrect value")

    def test_left13(self):
        self.setUp13()
        self.hero.move('left', self.village)
        self.assertEqual(self.hero.position, [11, 24], "incorrect value")

    def test_right13(self):
        self.setUp13()
        self.hero.move('right', self.village)
        self.assertEqual(self.hero.position, [11, 25], "incorrect value")

    def setUp14(self):
        self.hero = King([12, 23])
        self.village = village.createVillage(1)

    def test_up14(self):
        self.setUp14()
        self.hero.move('up', self.village)
        self.assertEqual(self.hero.position, [12, 23], "incorrect value")

    def test_down14(self):
        self.setUp14()
        self.hero.move('down', self.village)
        self.assertEqual(self.hero.position, [13, 23], "incorrect value")

    def test_left14(self):
        self.setUp14()
        self.hero.move('left', self.village)
        self.assertEqual(self.hero.position, [12, 22], "incorrect value")

    def test_right14(self):
        self.setUp14()
        self.hero.move('right', self.village)
        self.assertEqual(self.hero.position, [12, 24], "incorrect value")

    def setUp15(self):
        self.hero = King([6, 15])
        self.village = village.createVillage(1)

    def test_up15(self):
        self.setUp15()
        self.hero.move('up', self.village)
        self.assertEqual(self.hero.position, [5, 15], "incorrect value")

    def test_down15(self):
        self.setUp15()
        self.hero.move('down', self.village)
        self.assertEqual(self.hero.position, [7, 15], "incorrect value")

    def test_left15(self):
        self.setUp15()
        self.hero.move('left', self.village)
        self.assertEqual(self.hero.position, [6, 14], "incorrect value")

    def test_right15(self):
        self.setUp15()
        self.hero.move('right', self.village)
        self.assertEqual(self.hero.position, [6, 15], "incorrect value")

    def setUp16(self):
        self.hero = King([5, 16])
        self.village = village.createVillage(1)

    def test_up16(self):
        self.setUp16()
        self.hero.move('up', self.village)
        self.assertEqual(self.hero.position, [4, 16], "incorrect value")

    def test_down16(self):
        self.setUp16()
        self.hero.move('down', self.village)
        self.assertEqual(self.hero.position, [5, 16], "incorrect value")

    def test_left16(self):
        self.setUp16()
        self.hero.move('left', self.village)
        self.assertEqual(self.hero.position, [5, 15], "incorrect value")

    def test_right16(self):
        self.setUp16()
        self.hero.move('right', self.village)
        self.assertEqual(self.hero.position, [5, 17], "incorrect value")

    def setUp17(self):
        self.hero = King([9, 19])
        self.village = village.createVillage(1)

    def test_up17(self):
        self.setUp17()
        self.hero.move('up', self.village)
        self.assertEqual(self.hero.position, [8, 19], "incorrect value")

    def test_down17(self):
        self.setUp17()
        self.hero.move('down', self.village)
        self.assertEqual(self.hero.position, [10, 19], "incorrect value")

    def test_left17(self):
        self.setUp17()
        self.hero.move('left', self.village)
        self.assertEqual(self.hero.position, [9, 19], "incorrect value")

    def test_right17(self):
        self.setUp17()
        self.hero.move('right', self.village)
        self.assertEqual(self.hero.position, [9, 20], "incorrect value")

    def setUp18(self):
        self.hero = King([10, 18])
        self.village = village.createVillage(1)

    def test_up18(self):
        self.setUp18()
        self.hero.move('up', self.village)
        self.assertEqual(self.hero.position, [10, 18], "incorrect value")

    def test_down18(self):
        self.setUp18()
        self.hero.move('down', self.village)
        self.assertEqual(self.hero.position, [11, 18], "incorrect value")

    def test_left18(self):
        self.setUp18()
        self.hero.move('left', self.village)
        self.assertEqual(self.hero.position, [10, 17], "incorrect value")

    def test_right18(self):
        self.setUp18()
        self.hero.move('right', self.village)
        self.assertEqual(self.hero.position, [10, 19], "incorrect value")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMove))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    with open('output.txt', 'a') as file:
        file.write(str(result.wasSuccessful()).capitalize() + '\n')

province_name_th = {'TH-10':'กรุงเทพมหานคร', 'TH-11':'สมุทรปราการ', 'TH-12':'นนทบุรี', 'TH-13':'ปทุมธานี', 'TH-14':'พระนครศรีอยุธยา', 'TH-15':'อ่างทอง', 'TH-16':'ลพบุรี', 'TH-17':'สิงห์บุรี', 'TH-18':'ชัยนาท', 'TH-19':'สระบุรี', 'TH-20':'ชลบุรี', 'TH-21':'ระยอง', 'TH-22':'จันทบุรี', 'TH-23':'ตราด', 'TH-24':'ฉะเชิงเทรา', 'TH-25':'ปราจีนบุรี', 'TH-26':'นครนายก', 'TH-27':'สระแก้ว', 'TH-30':'นครราชสีมา', 'TH-31':'บุรีรัมย์', 'TH-32':'สุรินทร์', 'TH-33':'ศรีสะเกษ', 'TH-34':'อุบลราชธานี', 'TH-35':'ยโสธร', 'TH-36':'ชัยภูมิ', 'TH-37':'อำนาจเจริญ', 'TH-38':'บึงกาฬ', 'TH-39':'หนองบัวลำภู', 'TH-40':'ขอนแก่น', 'TH-41':'อุดรธานี', 'TH-42':'เลย', 'TH-43':'หนองคาย', 'TH-44':'มหาสารคาม', 'TH-45':'ร้อยเอ็ด', 'TH-46':'กาฬสินธุ์', 'TH-47':'สกลนคร', 'TH-48':'นครพนม', 'TH-49':'มุกดาหาร', 'TH-50':'เชียงใหม่', 'TH-51':'ลำพูน', 'TH-52':'ลำปาง', 'TH-53':'อุตรดิตถ์', 'TH-54':'แพร่', 'TH-55':'น่าน', 'TH-56':'พะเยา', 'TH-57':'เชียงราย', 'TH-58':'แม่ฮ่องสอน', 'TH-60':'นครสวรรค์', 'TH-61':'อุทัยธานี', 'TH-62':'กำแพงเพชร', 'TH-63':'ตาก', 'TH-64':'สุโขทัย', 'TH-65':'พิษณุโลก', 'TH-66':'พิจิตร', 'TH-67':'เพชรบูรณ์', 'TH-70':'ราชบุรี', 'TH-71':'กาญจนบุรี', 'TH-72':'สุพรรณบุรี', 'TH-73':'นครปฐม', 'TH-74':'สมุทรสาคร', 'TH-75':'สมุทรสงคราม', 'TH-76':'เพชรบุรี', 'TH-77':'ประจวบคีรีขันธ์', 'TH-80':'นครศรีธรรมราช', 'TH-81':'กระบี่', 'TH-82':'พังงา', 'TH-83':'ภูเก็ต', 'TH-84':'สุราษฎร์ธานี', 'TH-85':'ระนอง', 'TH-86':'ชุมพร', 'TH-90':'สงขลา', 'TH-91':'สตูล', 'TH-92':'ตรัง', 'TH-93':'พัทลุง', 'TH-94':'ปัตตานี', 'TH-95':'ยะลา', 'TH-96':'นราธิวาส', 'TH-S':'พัทยา'}
region_central = ['TH-10','TH-62','TH-18','TH-26','TH-73','TH-60','TH-12','TH-13','TH-14','TH-66','TH-65','TH-67','TH-16','TH-11','TH-75','TH-74','TH-19','TH-17','TH-64','TH-72','TH-15','TH-61']
region_north = ['TH-57', 'TH-50', 'TH-55', 'TH-56', 'TH-54', 'TH-58', 'TH-52', 'TH-51', 'TH-53']
region_northeast = ['TH-46', 'TH-40', 'TH-36', 'TH-48', 'TH-30', 'TH-38', 'TH-31', 'TH-44', 'TH-49', 'TH-35', 'TH-45', 'TH-42', 'TH-33', 'TH-47', 'TH-32', 'TH-43', 'TH-39', 'TH-37', 'TH-41', 'TH-34']
region_east = ['TH-22', 'TH-24', 'TH-20', 'TH-23', 'TH-25', 'TH-21', 'TH-27']
region_west = ['TH-71', 'TH-63', 'TH-77', 'TH-76', 'TH-70']
region_south = ['TH-81', 'TH-86', 'TH-92', 'TH-80', 'TH-96', 'TH-94', 'TH-82', 'TH-93', 'TH-83', 'TH-95', 'TH-85', 'TH-90', 'TH-91', 'TH-84']

def check_region(name):
    """check iso3166-2 and return region in thailand"""
    check = [c for c, n in province_name_th.items() if n == name].pop()
    return ("region_central" if check in region_central else
            "region_north" if check in region_north else
            "region_northeast" if check in region_northeast else
            "region_east" if check in region_east else
            "region_west" if check in region_west else
            "region_south")

def convert_to_th(name):
    """Convert name region thailand eng to thai"""
    return ("ภาคกลาง" if name == 'region_central' else
                "ภาคเหนือ" if name == 'region_north' else
                "ภาคตะวันออกเฉียงเหนือ" if name == 'region_northeast' else
                "ภาคตะวันออก" if name == 'region_east' else
                "ภาคตะวันตก" if name == 'region_west' else
                "ภาคใต้")

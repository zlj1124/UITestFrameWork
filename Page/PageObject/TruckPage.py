from Page.BasePage import BasePage
from util.parseConFile import ParseConFile
from config.conf import DATA_UploadFile
class TruckPage(BasePage):
    do_conf=ParseConFile()

    #导入按钮
    uploadfile_btn=do_conf.get_locators_or_account('TruckPageElements','uploadfile')
    upload_tip= do_conf.get_locators_or_account('TruckPageElements','uploadmsg')
    def uploadfile(self):
        #导入文件
        return self.send_keys(DATA_UploadFile,*TruckPage.uploadfile_btn)

    def  get_uploadmsg(self):
        return self.get_element_text(*TruckPage.upload_tip)
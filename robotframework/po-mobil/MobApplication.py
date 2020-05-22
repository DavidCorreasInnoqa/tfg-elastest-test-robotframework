# ------------------------------- Libraries ------------------------------- #
import json
import os

from robot.api.deco import keyword
from robotframework.po.common.PageObject import PageObject

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'


class MobApplication(PageObject):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Config ------------------------------- #
    def __init__(self):
        super().__init__('OutSystemsMobile')

    # ------------------------------- Keywords ------------------------------- #
    @keyword(name='Abrir aplicacion movil')
    def open_application(self, platform):
        # Recuperar la url en base al entorno
        current_path = os.path.dirname(os.path.abspath(__file__))
        with open(current_path + '/../data/MobCapabilities.json') as caps:
            capabilities = json.load(caps)

        self.osl.open_application(
            remote_url=self._get_remote_url_mob(), deviceName="emulator-5554",
            platformName=capabilities[platform]["platformName"], app=capabilities[platform]["app"],
            noReset=True, disableWindowAnimation=True, nativeWebScreenshot=True,
            androidScreenshotPath='results/screenshots',
            automationName=capabilities[platform]["automationName"], newCommandTimeout=60000)

        self.osl.switch_to_context(self.osl.get_contexts()[1])

    @keyword(name='Cerrar Aplicacion movil')
    def close_application(self):
        self.osl.quit_application()

    @keyword(name='Capturar Pantallazo movil')
    def capture_page_screenshot(self):
        self.osl.capture_page_screenshot()

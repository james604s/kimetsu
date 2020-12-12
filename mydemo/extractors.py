from mydemo.models import MaskData
from utils.logger import get_logger
logger = get_logger(__name__)

    # num_child = models.IntegerField(blank=True, null=True)
    # num_adult = models.IntegerField(blank=True, null=True)
    # agency_phone = models.CharField(max_length=-1, blank=True, null=True)
    # agency_name = models.CharField(max_length=-1, blank=True, null=True)
    # agency_code = models.CharField(max_length=-1, blank=True, null=True)
    # agency_address = models.CharField(max_length=-1, blank=True, null=True)
    # update_at = models.DateTimeField(blank=True, null=True)
    # city = models.CharField(max_length=-1, blank=True, null=True)
class MaskDataExtractors:
    def get_mask_data_by_city(self, city, ordering):
        type(ordering)
        query = {
            "city":city
        }
        try:
            result = list(MaskData.objects
                            .filter(**query) \
                            .values("agency_code", "agency_name", "agency_address", "agency_phone", "num_adult", "num_child", "update_at") \
                            .order_by(ordering))
            result=result[0:14]
            return result
        except Exception as e:
            logger.error(str(e))
            return []

    def get_mask_data_orderby_adult(self, city):
        query = {
            "city":city
        }
        try:
            result = list(GovMaskData.objects
                            .filter(**query) \
                            .values("agency_code", "name", "address", "phone", "mask_adult", "mask_child", "source_update")
                            .order_by("mask_adult"))
            return result
        except Exception as e:
            logger.error(str(e))
            return []

mask_data_extractors = MaskDataExtractors()
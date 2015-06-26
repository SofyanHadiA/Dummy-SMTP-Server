"""Mapper for Site Entity"""

from entity.geography import Site
from dal.sqa.mapping.dal_site import DalSite
from mapper.object_mapper import ObjectMapper

mapper = ObjectMapper()
mapper.create_map(DalSite, Site, "ToEntity")
mapper.create_map(Site, DalSite, "ToDal")

class SiteMapper:
    def __init__(self):
        """
        Constructor
        """
        self.__mapper = ObjectMapper()
        #self.__mapper.create_map(DalSite, Site, "ToEntity")
        #self.__mapper.create_map(Site, DalSite, "ToDal")


    def to_entity(self, dal_sites=DalSite):
        """
        Map Dal Site to Site Entity Object
        :param dal_sites: Dal Site object or list or tuple of Dal Site object
        :return: Site entity object
        """
        if dal_sites is DalSite:
            # ToDo: Change the map to use object mapper instead manual map if entity site exist
            site = object()
            site.site_id = dal_sites.site_id
            site.site_name = dal_sites.site_name
            site.city_id = dal_sites.city_id

            return site

        if dal_sites is list \
                or dal_sites is tuple \
                or hasattr(dal_sites, "__len__"):

            sites = []
            for dal_site in dal_sites:
                site = Site()
                site.site_id = dal_site.site_id
                site.site_name = dal_site.site_name
                site.city_id = dal_site.city_id

                sites.append(site)

            return sites

        # else throw exception
        raise ValueError('Parameter type %s is not supported' % dal_sites)


    def to_dal(self, site=Site):
        """
        Map Site Entity to Dal Entity
        :param site: Site entity object
        :return:
        """
        dal_site = DalSite()
        dal_site.site_id = site.site_id
        dal_site.site_name = site.site_name
        dal_site.city_id = site.city_id

        return dal_site

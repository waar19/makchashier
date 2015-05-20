from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from androidwebservices.models import Usuario
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.http import HttpApplicationError
from tastypie import fields
from tastypie.utils import trailing_slash
from django.conf.urls import url
from django.conf import settings

class UsuarioResource(ModelResource):
    class Meta:
        queryset = Usuario.objects.all()
        resource_name = 'usuario'
        excludes = ['clave', 'fecha']
        authentication = BasicAuthentication()

	def override_urls(self):
		return [
			url(r"^(?P<resource_name>%s)/login%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('login'), name="api_login"),
		]

	def login(self, request, **kwargs):
		try:
			user = Usuario.objects.filter(activo=1)
		except Usuario.DoesNotExist:
			return self.create_response(request, {
					'No user'
				})
		else:
			user_object = []
			for user in users:
				user_object.append(user.to_object())
			return self.create_response(request, user_object)
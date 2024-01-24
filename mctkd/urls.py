from rest_framework import routers
from .api import SedeViewSet, ApoderadoViewSet, CategoriaViewSet, CinturonViewSet, ProfesorViewSet, HorarioViewSet, AlumnoViewSet, PensionViewSet

router = routers.DefaultRouter()

router.register('api/sede', SedeViewSet, 'sedes')
router.register('api/apoderado', ApoderadoViewSet, 'apoderados')
router.register('api/categoria', CategoriaViewSet, 'categorias')
router.register('api/cinturon', CinturonViewSet, 'cinturones')
router.register('api/profesor', ProfesorViewSet, 'profesores')
router.register('api/horario', HorarioViewSet, 'horarios')
router.register('api/alumno', AlumnoViewSet, 'alumnos')
router.register('api/pension', PensionViewSet, 'pensiones')

urlpatterns =router.urls
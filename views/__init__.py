from flask import Blueprint
app_views=Blueprint('app_views',__name__)
from views.downloadCsv import *
from views.downloadXlsx import *
from views.demandes import *
from views.demandesMA import *
from views.latestData import *
from views.graphData import *
from views.user import *
from views.dashboard import *

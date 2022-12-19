# Работа в модели Revit с использованием RevitPythonShell
# Назначение: присваивание колоннам конструкции марок в зависимости
# от наименования осей.
# Последовательность работы:
# 1. Выделяем нужные колонны в модели Revit;
# 2. Запускаем скрипт в Revit;
# 3. Проверяем наименование марок колонн.

# Импорт RevitAPI.dll
from Autodesk.Revit.DB import *

# Доступ к активному документу Revit
uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

# Идентификаторы выделенных вручную элементов
ids = uidoc.Selection.GetElementIds()

# Перевод идентификаторов в элементы
elems = []
for i in ids:
	strId = str(i)
	intId = int(strId)
	elId = ElementId(intId)
	el = doc.GetElement(elId)
	elems.append(el)

# Фильтр колонн
columns = []
for i in elems:
	if i.Category.Name == 'Несущие колонны':
		locPt = i.Location.Point
		param = i.LookupParameter('Марка')
		columns.append([locPt, param])

# Сортировка по функции
def srt(x):
	return (x[0][1],  x[0][0])

sortCol = sorted(columns, key = srt, reverse = True)

# Открываем транзакцию, записываем информацию в марки, закрываем транзакцию
t = Transaction(doc, 'SetParam')
t.Start()

for i,k in enumerate(sortCol):
	k[1].Set('К' + str(i+1))

t.Commit()

__window__.Close()
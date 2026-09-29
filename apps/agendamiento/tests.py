from datetime import date, time

from django.test import SimpleTestCase

from . import calendario as cal


def _evento(inicio, fin, categoria=cal.CATEGORIA_CONSULTA, fecha=date(2026, 9, 21)):
    return cal.Evento(
        fecha=fecha, inicio=inicio, fin=fin, titulo="Firulais",
        detalle="", servicio="", categoria=categoria,
    )


class CalendarioHU08Tests(SimpleTestCase):
    """HU08 / RF26: lógica del calendario visual."""

    def test_categoria_por_tipo_servicio(self):
        self.assertEqual(cal.categoria_de("peluqueria"), cal.CATEGORIA_PELUQUERIA)
        self.assertEqual(cal.categoria_de("vacunacion"), cal.CATEGORIA_CONSULTA)
        self.assertEqual(cal.categoria_de("consulta_general"), cal.CATEGORIA_CONSULTA)

    def test_inicio_semana_es_lunes(self):
        self.assertEqual(cal.inicio_semana(date(2026, 9, 27)), date(2026, 9, 21))
        self.assertEqual(cal.inicio_semana(date(2026, 9, 21)), date(2026, 9, 21))

    def test_posicion_vertical(self):
        e = _evento(time(8, 0), time(9, 0))
        cal.distribuir([e], 7, 20)
        self.assertAlmostEqual(e.top, 100 / 13, places=2)
        self.assertAlmostEqual(e.alto, 100 / 13, places=2)

    def test_citas_solapadas_en_columnas(self):
        a = _evento(time(9, 0), time(10, 0))
        b = _evento(time(9, 30), time(10, 30))
        c = _evento(time(11, 0), time(11, 30))
        cal.distribuir([a, b, c], 7, 20)
        self.assertEqual((a.columna, a.columnas), (0, 2))
        self.assertEqual((b.columna, b.columnas), (1, 2))
        self.assertEqual((c.columna, c.columnas), (0, 1))

    def test_rango_horas_se_amplia(self):
        eventos = [_evento(time(6, 30), time(7, 0)), _evento(time(20, 0), time(20, 45))]
        self.assertEqual(cal.rango_horas(eventos), (6, 21))
        self.assertEqual(cal.rango_horas([]), (7, 20))

    def test_construir_dias_agrupa_por_fecha(self):
        lunes = date(2026, 9, 21)
        fechas = [lunes, date(2026, 9, 22)]
        eventos = [
            _evento(time(9, 0), time(10, 0), fecha=lunes),
            _evento(time(9, 0), time(10, 0), cal.CATEGORIA_PELUQUERIA, fecha=date(2026, 9, 22)),
            _evento(time(9, 0), time(10, 0), fecha=date(2026, 9, 30)),  # fuera de rango
        ]
        dias = cal.construir_dias(eventos, fechas, 7, 20)
        self.assertEqual([len(d.eventos) for d in dias], [1, 1])
        self.assertEqual(dias[1].eventos[0].categoria, cal.CATEGORIA_PELUQUERIA)

    def test_titulo_rango(self):
        semana = [date(2026, 9, 21 + i) for i in range(7)]
        self.assertEqual(cal.titulo_rango("semana", semana), "21 – 27 de septiembre de 2026")
        self.assertEqual(cal.titulo_rango("dia", [date(2026, 9, 27)]), "Domingo 27 de septiembre de 2026")

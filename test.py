import unittest
from chronopost.ChronopostService import ChronopostService
from chronopost.Order import Order

class ChronopostTest(unittest.TestCase):
    def setUp(self):
        self.chronopost_service = ChronopostService()

    def tearDown(self):
        pass

    def testGetHeader(self):
        header = self.chronopost_service.get_header()

        self.assertEqual(header,
                         'account;dest_code;dest_name;dest_address;dest_pcode;dest_pcodelocal;dest_country;dest_telef;dest_mobile_telef;Dest_email;dest_contact;ship_weight;ship_label_of;ship_cod;ship_clientref;ship_descr;'
                         )

    def testCreateNewOrder(self):
        order = Order(account='a', dest_name='a', dest_address='a', dest_pcode='a', dest_pcodelocal='a',
                      dest_country='a', dest_mobile_telef='a', Dest_email='a', ship_weight='a',
                      ship_label_of='a', ship_cod='a')

        self.assertIsNotNone(order)
        self.assertEqual('a', order.account)
        self.assertEqual('a', order.dest_name)
        self.assertEqual('a', order.dest_address)
        self.assertEqual('a', order.dest_pcode)
        self.assertEqual('a', order.dest_pcodelocal)
        self.assertEqual('a', order.dest_country)
        self.assertEqual('a', order.dest_mobile_telef)
        self.assertEqual('a', order.Dest_email)
        self.assertEqual('a', order.ship_weight)
        self.assertEqual('a', order.ship_label_of)
        self.assertEqual('a', order.ship_cod)
        self.assertIsNone(order.dest_code)
        self.assertIsNone(order.dest_telef)
        self.assertIsNone(order.dest_contact)
        self.assertIsNone(order.ship_clientref)
        self.assertIsNone(order.ship_descr)

        order = Order(account='b', dest_name='b', dest_address='b', dest_pcode='b', dest_pcodelocal='b',
                      dest_country='b', dest_mobile_telef='b', Dest_email='b', ship_weight='b',
                      ship_label_of='b', ship_cod='b', dest_code='b')

        self.assertIsNotNone(order)
        self.assertEqual('b', order.account)
        self.assertEqual('b', order.dest_name)
        self.assertEqual('b', order.dest_address)
        self.assertEqual('b', order.dest_pcode)
        self.assertEqual('b', order.dest_pcodelocal)
        self.assertEqual('b', order.dest_country)
        self.assertEqual('b', order.dest_mobile_telef)
        self.assertEqual('b', order.Dest_email)
        self.assertEqual('b', order.ship_weight)
        self.assertEqual('b', order.ship_label_of)
        self.assertEqual('b', order.ship_cod)
        self.assertIsNotNone(order.dest_code)
        self.assertEqual('b', order.dest_code)
        self.assertIsNone(order.dest_telef)
        self.assertIsNone(None, order.dest_contact)
        self.assertIsNone(None, order.ship_clientref)
        self.assertIsNone(None, order.ship_descr)

    def testGetRow(self):
        order1 = Order(account='09990001', dest_code='2222', dest_name='NOME DO DESTINATARIO',
                       dest_address='ENDERECO DO DESTINATARIO',
                       dest_pcode='2100-001', dest_pcodelocal='LISBOA', dest_country='PT',
                       dest_telef='212233449', dest_mobile_telef='912255455', Dest_email='a@b.c',
                       dest_contact='CONTACTO', ship_weight='1', ship_label_of='3', ship_cod='120,00',
                       ship_clientref='NUMERO DE FACTURA', ship_descr='DESCRICAO DO ENVIO')

        row = self.chronopost_service.get_row(order1)

        expected = '09990001;2222;NOME DO DESTINATARIO;ENDERECO DO DESTINATARIO;2100-001;LISBOA;PT;212233449;912255455;a@b.c;CONTACTO;1;3;120,00;NUMERO DE FACTURA;DESCRICAO DO ENVIO\n'

        self.assertEqual(expected, row)


    def testGetChronopostFile(self):
        order1 = Order(account='09990001', dest_code='2222', dest_name='NOME DO DESTINATARIO', dest_address='ENDERECO DO DESTINATARIO',
                        dest_pcode='2100-001', dest_pcodelocal='LISBOA', dest_country='PT',
                        dest_telef='212233449', dest_mobile_telef='912255455', Dest_email='a@b.c',
                        dest_contact='CONTACTO', ship_weight='1', ship_label_of='3', ship_cod='120,00',
                        ship_clientref='NUMERO DE FACTURA', ship_descr='DESCRICAO DO ENVIO')
        order2 = Order(account='09990002', dest_code='6788', dest_name='NOME DO DESTINATARIO',
                       dest_address='ENDERECO DO DESTINATARIO',
                       dest_pcode='3000-001', dest_pcodelocal='COIMBRA', dest_country='PT',
                       dest_telef='232233455', dest_mobile_telef='912255455', Dest_email='a@b.c',
                       dest_contact='CONTACTO', ship_weight='1', ship_label_of='1', ship_cod='0,00',
                       ship_clientref='NUMERO DE FACTURA', ship_descr='DESCRICAO DO ENVIO')
        order3 = Order(account='09990004', dest_code='55555', dest_name='NOME DO DESTINATARIO',
                       dest_address='ENDERECO DO DESTINATARIO',
                       dest_pcode='30000', dest_pcodelocal='MADRID', dest_country='ES',
                       dest_telef='0034232233455', dest_mobile_telef='0034912255455', Dest_email='a@b.c',
                       dest_contact='CONTACTO', ship_weight='1', ship_label_of='1', ship_cod='0,00',
                       ship_clientref='NUMERO DE FACTURA', ship_descr='DESCRICAO DO ENVIO')

        orders = [order1, order2, order3]

        file = self.chronopost_service.get_chronopost_file(orders)

        input = '''09990001;2222;NOME DO DESTINATARIO;ENDERECO DO DESTINATARIO;2100-001;LISBOA;PT;212233449;912255455;a@b.c;CONTACTO;1;3;120,00;NUMERO DE FACTURA;DESCRICAO DO ENVIO
09990002;6788;NOME DO DESTINATARIO;ENDERECO DO DESTINATARIO;3000-001;COIMBRA;PT;232233455;912255455;a@b.c;CONTACTO;1;1;0,00;NUMERO DE FACTURA;DESCRICAO DO ENVIO
09990004;55555;NOME DO DESTINATARIO;ENDERECO DO DESTINATARIO;30000;MADRID;ES;0034232233455;0034912255455;a@b.c;CONTACTO;1;1;0,00;NUMERO DE FACTURA;DESCRICAO DO ENVIO
'''

        self.assertIsNotNone(file)
        self.assertEqual(input, file)
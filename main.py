#!/usr/bin/env python
#-*- coding: utf-8 -*-


# Obs: Need to install pygtk on windows
import pygtk
pygtk.require("2.0") #Essa linha define a versão do pygtk a ser importado
import gtk
from bet_calculator.bet_calculator import Bet_Calculator

from decimal import *

class Vision(object):
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("calculadorApostas.glade")

        self.calculador_de_aposta = Bet_Calculator()

        builder.connect_signals({
            "gtk_main_quit": gtk.main_quit,
            
            "on_txTime1_activate": self.time1_preenchido,
            "on_txTime1_focus_out_event": self.time1_preenchido,
            
            "on_txTime2_activate": self.time2_preenchido,
            "on_txTime2_focus_out_event": self.time2_preenchido,

            "on_txCasa1_activate": self.casa1_preenchido,
            "on_txCasa1_focus_out_event": self.casa1_preenchido,

            "on_txCasa2_activate": self.casa2_preenchido,
            "on_txCasa2_focus_out_event": self.casa2_preenchido,

            "on_txCotacaoTime1Casa1_activate": self.cotacao_time1_casa1_preenchido,
            "on_txCotacaoTime1Casa1_focus_out_event": self.cotacao_time1_casa1_preenchido,

            "on_txCotacaoTime1Casa2_activate": self.cotacao_time1_casa2_preenchido,
            "on_txCotacaoTime1Casa2_focus_out_event": self.cotacao_time1_casa2_preenchido,

            "on_txCotacaoTime2Casa1_activate": self.cotacao_time2_casa1_preenchido,
            "on_txCotacaoTime2Casa1_focus_out_event": self.cotacao_time2_casa1_preenchido,

            "on_txCotacaoTime2Casa2_activate": self.cotacao_time2_casa2_preenchido,
            "on_txCotacaoTime2Casa2_focus_out_event": self.cotacao_time2_casa2_preenchido,

            "on_txValorTotal_activate": self.valor_total_preenchido,
            "on_txValorTotal_focus_out_event": self.valor_total_preenchido,

            "on_hsTimes_move_slider": self.slider_modificado,
            "on_hsTimes_value_changed": self.slider_modificado,

            "on_rbTime1Casa1_toggled": self.bet_team1_house1_ativado,
            "on_rbTime1Casa2_toggled": self.aposta_time1_casa2_ativado,
        })

        self.Time1 = "Time 1"
        self.Time2 = "Time 2"
        self.Casa1 = "Casa 1"
        self.Casa2 = "Casa 2"

        self.frmprincipal = builder.get_object("frmPrincipal") #form Principal, será exibido somente
        
        self.txTime1 = builder.get_object("txTime1") # Texto onde captura o time 1
        self.txTime2 = builder.get_object("txTime2") # Texto onde captura o time 2
        self.txCasa1 = builder.get_object("txCasa1") # Texto onde captura a casa 1
        self.txCasa2 = builder.get_object("txCasa2") # Texto onde captura a casa 2
        
        self.lbNumeroTime1 = builder.get_object("lbNumeroTime1")
        self.lbNumeroTime2 = builder.get_object("lbNumeroTime2")
        self.lbNumeroCasa1 = builder.get_object("lbNumeroCasa1")
        self.lbNumeroCasa2 = builder.get_object("lbNumeroCasa2")
        
        self.rbTime1Casa1 = builder.get_object("rbTime1Casa1")
        self.rbTime1Casa2 = builder.get_object("rbTime1Casa2")
        
        self.lbResultadoTime1 = builder.get_object("lbResultadoTime1")
        self.lbResultadoTime2 = builder.get_object("lbResultadoTime2")
        
        self.lbVencedorTime1 = builder.get_object("lbVencedorTime1")
        self.lbVencedorTime2 = builder.get_object("lbVencedorTime2")
        
        self.lbAvisaNumeros = builder.get_object("lbAvisaNumeros")
        
        self.txCotacaoTime1Casa1 = builder.get_object("txCotacaoTime1Casa1")
        self.txCotacaoTime2Casa1 = builder.get_object("txCotacaoTime2Casa1")
        self.txCotacaoTime1Casa2 = builder.get_object("txCotacaoTime1Casa2")
        self.txCotacaoTime2Casa2 = builder.get_object("txCotacaoTime2Casa2")

        self.hsTimesValores = builder.get_object("hsTimesValores")
        self.txValorTime1 = builder.get_object("txValorTime1")
        self.txValorTime2 = builder.get_object("txValorTime2")

        self.txValorTotal = builder.get_object("txValorTotal")

        self.lbLucroTime1Vencedor = builder.get_object("lbLucroTime1Vencedor")
        self.lbLucroTime2Vencedor = builder.get_object("lbLucroTime2Vencedor")

        self.hsTimes = builder.get_object("hsTimes")

        self.frmprincipal.show()

    def time1_preenchido(self, widget, never_used=''):
        time1 = self.txTime1.get_text()

        if time1 != '':
            self.Time1 = time1
        else:
            self.Time1 = 'Time 1'

        self.preenche_dados_time1()

    def time2_preenchido(self, widget, never_used=''):
        time2 = self.txTime2.get_text()

        if time2 != '':
            self.Time2 = time2
        else:
            self.Time2 = 'Time 2'


        self.preenche_dados_time2()

    def casa1_preenchido(self, widget, never_used=''):
        casa1 = self.txCasa1.get_text()

        if casa1 != '':
            self.Casa1 = casa1
        else:
            self.Casa1 = 'Casa 1'

        self.preenche_dados_casa1()

    def casa2_preenchido(self, widget, never_used=''):
        casa2 = self.txCasa2.get_text()

        if casa2 != '':
            self.Casa2 = casa2
        else:
            self.Casa2 = 'Casa 2'
        
        self.preenche_dados_casa2()

    def cotacao_time1_casa1_preenchido(self, widget, never_used=''):
        try:
            self.calculador_de_aposta.decimal_team1_house1 = self.txCotacaoTime1Casa1.get_text()
        except:
            self.calculador_de_aposta.decimal_team1_house1 = 0

        self.atualiza_informacoes_apostas()

    def cotacao_time1_casa2_preenchido(self, widget, never_used=''):
        try:
            self.calculador_de_aposta.decimal_team1_house2 = self.txCotacaoTime1Casa2.get_text()
        except:
            self.calculador_de_aposta.decimal_team1_house2 = 0

        self.atualiza_informacoes_apostas()

    def cotacao_time2_casa1_preenchido(self, widget, never_used=''):
        try:
            self.calculador_de_aposta.decimal_team2_house1 = self.txCotacaoTime2Casa1.get_text()
        except:
            self.calculador_de_aposta.decimal_team2_house1 = 0

        self.atualiza_informacoes_apostas()

    def cotacao_time2_casa2_preenchido(self, widget, never_used=''):
        try:
            self.calculador_de_aposta.decimal_team2_house2 = self.txCotacaoTime2Casa2.get_text()
        except:
            self.calculador_de_aposta.decimal_team2_house2 = 0

        self.atualiza_informacoes_apostas()

    def valor_total_preenchido(self, widget, never_used=''):
        try:
            self.calculador_de_aposta.cash_to_bet = self.txValorTotal.get_text()
        except:
            self.calculador_de_aposta.cash_to_bet = 0

        self.atualiza_informacoes_apostas()

    def slider_modificado(self, widget, never_used=''):
        self.atualiza_informacoes_de_lucro()

    def bet_team1_house1_ativado(self, widget, never_used=''):
        if self.rbTime1Casa1.get_active() and (not self.rbTime1Casa1.get_property("inconsistent") ):
            self.hsTimes.set_value(0)
            self.atualiza_informacoes_de_lucro()
        else:
            if (not self.rbTime1Casa2.get_property("inconsistent") ):
                self.rbTime1Casa2.set_active(True)

    def aposta_time1_casa2_ativado(self, widget, never_used=''):
        if self.rbTime1Casa2.get_active() and (not self.rbTime1Casa2.get_property("inconsistent") ):
            self.hsTimes.set_value(0)
            self.atualiza_informacoes_de_lucro()
        else:
            if (not self.rbTime1Casa1.get_property("inconsistent") ):
                self.rbTime1Casa1.set_active(True)

    
    def preenche_dados_time1(self):
        self.lbNumeroTime1.set_text(self.Time1)
        self.atualiza_radio_buttons()
        self.lbResultadoTime1.set_text(self.Time1)
        self.lbVencedorTime1.set_text("Se " + self.Time1 + " ganhar")

    def preenche_dados_time2(self):
        self.lbNumeroTime2.set_text(self.Time2)
        self.atualiza_radio_buttons()
        self.lbResultadoTime2.set_text(self.Time2)
        self.lbVencedorTime2.set_text("Se " + self.Time2 + " ganhar")

    def preenche_dados_casa1(self):
        self.lbNumeroCasa1.set_text(self.Casa1)
        self.atualiza_radio_buttons()

    def preenche_dados_casa2(self):
        self.lbNumeroCasa2.set_text(self.Casa2)
        self.atualiza_radio_buttons()

    def atualiza_radio_buttons(self):
        self.rbTime1Casa1.set_label(
            self.preencheDadosCasaTime(self.Time1, self.Casa1, self.Time2, self.Casa2)
        )
        self.rbTime1Casa2.set_label(
            self.preencheDadosCasaTime(self.Time1, self.Casa2, self.Time2, self.Casa1)
        )

    def preencheDadosCasaTime(self, time1, casa1, time2, casa2):
        return time1 + " => " + casa1 + " / " + time2 +" => " + casa2

    def atualiza_informacoes_de_lucro(self):
        valor_time1 = Decimal('0.0')
        valor_time2 = Decimal('0.0')

        proporcao = Decimal(self.hsTimes.get_value())/Decimal('100');

        if self.rbTime1Casa1.get_active() and (not self.rbTime1Casa1.get_property("inconsistent") ):
            maximo_valor_time1 = self.calculador_de_aposta.biggest_possible_value_team1(bet_team1_house1 = True)
            minimo_valor_time1 = self.calculador_de_aposta.least_possible_value_team1(bet_team1_house1 = True)

            diferenca = maximo_valor_time1 - minimo_valor_time1

            valor_proporcao = proporcao*diferenca

            valor_time1 = minimo_valor_time1+valor_proporcao
            valor_time2 = self.calculador_de_aposta.cash_to_bet - valor_time1

            self.txValorTime1.set_text(("%.2f" % valor_time1))
            self.txValorTime2.set_text(("%.2f" % valor_time2))

        elif self.rbTime1Casa2.get_active() and (not self.rbTime1Casa2.get_property("inconsistent") ):
            maximo_valor_time1 = self.calculador_de_aposta.biggest_possible_value_team1(bet_team1_house1 = False)
            minimo_valor_time1 = self.calculador_de_aposta.least_possible_value_team1(bet_team1_house1 = False)

            diferenca = maximo_valor_time1 - minimo_valor_time1

            valor_proporcao = proporcao*diferenca

            valor_time1 = minimo_valor_time1+valor_proporcao
            valor_time2 = self.calculador_de_aposta.cash_to_bet - valor_time1
            self.txValorTime1.set_text(("%.2f" % valor_time1))
            self.txValorTime2.set_text(("%.2f" % valor_time2))

        if valor_time1 > 0:
            lucroTime1 = 0.0
            lucroTime2 = 0.0
            if self.rbTime1Casa1.get_active() and (not self.rbTime1Casa1.get_property("inconsistent") ):
                lucroTime1 = self.calculador_de_aposta.profit_if_team1_wins(valor_time1, bet_team1_house1 = True)
                lucroTime2 = self.calculador_de_aposta.profit_if_team2_wins(valor_time2, bet_team1_house1 = True)
            elif self.rbTime1Casa2.get_active() and (not self.rbTime1Casa2.get_property("inconsistent") ):
                lucroTime1 = self.calculador_de_aposta.profit_if_team1_wins(valor_time1, bet_team1_house1 = False)
                lucroTime2 = self.calculador_de_aposta.profit_if_team2_wins(valor_time2, bet_team1_house1 = False)

            self.lbLucroTime1Vencedor.set_text(("%.2f" % lucroTime1))
            self.lbLucroTime2Vencedor.set_text(("%.2f" % lucroTime2))
        else:
            self.lbLucroTime1Vencedor.set_text("0.0")
            self.lbLucroTime2Vencedor.set_text("0.0")

    def atualiza_informacoes_apostas(self):
        str_final = ""
        
        if self.calculador_de_aposta.can_bet_team1_house1:
            str_final += ("É possível fazer apostas\ncom o " + 
                self.Time1 + " no site\n" + self.Casa1 + " e o " +
                self.Time2 + "\n" + "no site " + self.Casa2) +"\n"
            self.rbTime1Casa1.set_property("inconsistent", False)
        else:
            self.rbTime1Casa1.set_property("inconsistent", True)
            self.rbTime1Casa2.set_active(True)

        if self.calculador_de_aposta.can_bet_team1_house2:
            str_final += ("É possível fazer apostas\ncom o " + 
                self.Time1 + " no site\n" + self.Casa2 + " e o " +
                self.Time2 + "\n" + "no site " + self.Casa1) +"\n"
            self.rbTime1Casa2.set_property("inconsistent", False)
        else:
            self.rbTime1Casa2.set_property("inconsistent", True)

        self.hsTimes.set_value(0)
        self.atualiza_informacoes_de_lucro()
        
        self.lbAvisaNumeros.set_text(str_final)

if __name__ == "__main__":
    app = Vision()
    gtk.main()
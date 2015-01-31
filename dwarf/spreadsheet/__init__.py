# -*- coding: utf-8 -*-
import getpass
import gdata.spreadsheet.service

class SpreadSheet():

    def __init__(self, title, email, password):
        self.__title = title
        self.__client = gdata.spreadsheet.service.SpreadsheetsService()
        self.__client.ClientLogin(email, password)
        self.__client.ProgrammaticLogin()

        spreadsheets = self.__client.GetSpreadsheetsFeed()

        for spreadsheet_entry in spreadsheets.entry:
            if spreadsheet_entry.title.text == self.__title:
                self.__key = spreadsheet_entry.id.text.rsplit('/')[-1]
                worksheet = self.__client.GetWorksheetsFeed(self.__key).entry[0]
                self.__worksheet_key = worksheet.id.text.rsplit('/')[-1]

    def insert_link(self, link, title):
        row = {'link': link, 'title': title}
        self.__client.InsertRow(row, self.__key, self.__worksheet_key)


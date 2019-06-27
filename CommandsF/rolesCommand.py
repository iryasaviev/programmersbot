class RolesCommand:

    @property
    def message(self):
        return '——— Роли сервера ———\n\nРоли на сервере разделены на несколько пунктов, а те, в свою очередь, ещё на несколько подпунктов. Наличие той или иной роли у участника свидетельствует о его принадлежности к той или иной области.\n\nНа сервере присутствуют роли независимые от какой-либо иной конкретно. К таким ролям относятся:\n— Указывающие уровень опыта и знаний в той или иной области:\n     1. `junior` — новичок, младший;\n     2. `middle` — средний;\n     3. `senior` — старший.\n— Указывающие, что участник является ботом:\n     1. — `Bot` — бот.\n\nПодробнее на канале: `🤵-roles` (https://discord.gg/uSYHC2C).'

    def sendResult(self):
        return self.message
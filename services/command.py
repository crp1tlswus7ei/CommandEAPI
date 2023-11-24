from models.command import Command as CommandModel
from schemas.command import Command

class CommandService():

    def __init__(self, db) -> None:
        self.db = db

    def get_commands(self):
        result = self.db.query(CommandModel).all()
        return result 
        
    def get_command(self, id):
        result = self.db.query(CommandModel).filter(CommandModel.id == id).first()
        return result
        
    def get_command_by_category(self, category):
        result = self.db.query(CommandModel).filter(CommandModel.category == category).all()
        return result
    
    def create_command(self, command: Command):
        new_command = CommandModel(**command.model_dump())
        self.db.add(new_command)
        self.db.commit()
        return
    
    def update_command(self, id: int, data: Command):
        command = self.db.query(CommandModel).filter(CommandModel.id == id).first()
        command.title = data.title
        command.overview = data.overview
        command.category = data.category
        self.db.add(command) # Añadiendo los resultados
        self.db.commit() # Mandando los resultados a la base de datos
        # se elimino refres por causas de errores
        return
    
    def delete_command(self, id: int):
        self.db.query(CommandModel).filter(CommandModel.id == id).delete()
        self.db.commit()
        return
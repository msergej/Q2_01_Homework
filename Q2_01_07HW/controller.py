import OwnFunctions as OFs
import model
import view
import logger

def phone_list():
    operation = OFs.input_natural_number("Введите код операции: 1 - запись в справочник, 2 - поиск в справочнике, 9 - завершение работы: ")
    while operation<3 :
        match operation:
            case 1: 
                new_dataset = model.get_new_phone_number()
                if len(str(new_dataset)) > 1 :
                    print("Абонент будет внесен в список.")     
                    view.show_list_entry(new_dataset)
                    logger.add_list_entry(new_dataset)
                    logger.log_request(1, new_dataset)
                else : print("Абонент с таким номером уже присутсвует в списке.")

            case 2:
                search_result = model.find_phone_number()
                if len(str(search_result)) > 1 :
                    print("Абонент обнаружен в списке.")     
                    view.show_list_entry(search_result)                
                logger.log_request(0, search_result)
            case _: 
                print("Заданного кода операции не существует.")

        operation = OFs.input_natural_number("Введите код операции: 1 - запись в справочник, 2 - поиск в справочнике, 9 - завершение работы: ")
    return "Работа с телефонным справочником завершена."
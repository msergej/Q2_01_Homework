import view
import model
import logger

def run_calc():
    mode = view.choose()
    while(mode != 9):
        if mode == 1 :
            expr = view.get_expr(mode)
            result = model.execute_expr(expr)
            view.show_res(result)
            logger.log_exec(expr, result)
            mode = view.choose()
        elif mode == 2 :
            expr = view.get_expr(mode)
            result = model.solve_eq(expr)
            view.show_res(result)
            logger.log_exec(expr, result)
            mode = view.choose()
        elif mode == 3 : 
            expr = view.get_expr(mode)
            result = model.simpify_pol(expr)
            view.show_res(result)
            logger.log_exec(expr, result)
            mode = view.choose()
        elif mode == 4 :
            history = logger.get_history()
            view.show_history(history)
            mode = view.choose()
        elif mode == 9 :
            view.exit()
        else:
            view.erorr_mode()
            mode = view.choose()
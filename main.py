
import dearpygui.dearpygui as dpg

dpg.create_context()
count = 2
last_pos = []


def add_point(user_data):
    if dpg.get_value('mode') == 'default graphics':
        pass
    else:
        global count
        count += 1
        dpg.add_input_text(label=f"Dot {count}", parent=user_data, tag=f'c_{count}', width=100)

        dpg.delete_item(item='btn_close')
        dpg.add_button(label='Add dot', callback=add_point, user_data='Main', tag='btn_close', parent=user_data)


def create_painting(user_data):
    with dpg.window(label='second',no_resize=True, no_move=True, no_collapse=True):
        with dpg.drawlist(width=600, height=600):
            for i in range(1, count):
                x = [int(i)*5 for i in dpg.get_value(item=f'c_{i}').split()]
                y = [int(i)*5 for i in dpg.get_value(item=f'c_{i + 1}').split()]
                dpg.draw_line(p1=x, p2=y, color=(255, 255, 255), thickness=2)


with dpg.window(label='Function', tag='Main', width=600, height=600, no_resize=True, no_move=True, no_title_bar=True, no_collapse=True):
    dpg.add_button(label='Create Painting', callback=create_painting)
    dpg.add_input_text(label='Dot 1', tag='c_1', width=100)
    dpg.add_input_text(label='Dot 2', tag='c_2', width=100)
    dpg.add_button(label='Add dot', callback=add_point, user_data='Main', tag='btn_close')

dpg.create_viewport(title='Paintinger', width=600, height=600, resizable=False)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

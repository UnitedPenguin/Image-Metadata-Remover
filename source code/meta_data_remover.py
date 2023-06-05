import os
import piexif
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

KV = '''
<Content>:
    orientation: "vertical"
    spacing: "12dp"

    MDLabel:
        text: "Image Metadata Remover"
        theme_text_color: "Secondary"
        halign: 'center'
        font_style: 'H5'

    MDLabel:
        text: "Drop Images Here"
        theme_text_color: "Secondary"
        halign: 'center'
        font_style: 'H4'
        bold: True
        color: 0, 0, 0, 1  # Black color

    MDLabel:
        text: "Drag and Drop Images onto this Window"
        theme_text_color: "Secondary"
        halign: 'center'
'''


def remove_metadata(image_path):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    image_filename = os.path.splitext(os.path.basename(image_path))[0] + "_no_metadata" + os.path.splitext(image_path)[1]
    output_image_path = os.path.join(script_dir, image_filename)

    if os.path.splitext(image_path)[1].lower() in ['.jpg', '.jpeg']:
        piexif.remove(image_path, output_image_path)
    elif os.path.splitext(image_path)[1].lower() in ['.png', '.gif', '.tiff']:
        from PIL import Image
        image = Image.open(image_path)
        image.save(output_image_path)

    return output_image_path


class Content(BoxLayout):
    pass


class RemoveMetadataApp(MDApp):
    dialog = None
    startup_dialog = None

    def build(self):
        self.icon = 'your_app_icon.png'  # you can add an icon for the app here
        self.theme_cls.primary_palette = "Teal"  # "Teal", "Red"
        return Builder.load_string(KV)

    def on_start(self):
        info_text = "This program allows you to remove metadata from images. To use it, simply drag and drop an image file (JPEG, PNG, GIF, or TIFF) onto this window. The processed image will be saved in the same directory as this program, with '_no_metadata' added to the original filename."
        self.startup_dialog = MDDialog(
            title='Welcome to Image Metadata Remover',
            text=info_text,
            buttons=[MDFlatButton(text='OK', on_release=self.startup_dialog_close)]
        )
        self.startup_dialog.open()

    def startup_dialog_close(self, *args):
        Window.bind(on_dropfile=self.on_file_drop)
        self.startup_dialog.dismiss(force=True)

    def on_file_drop(self, window, file_path):
        file_path = file_path.decode('utf-8')
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1].lower() in ['.jpg', '.jpeg', '.png', '.gif', '.tiff']:
            try:
                output_path = remove_metadata(file_path)
                info = f"Metadata removed from image. Saved as {output_path}"
            except Exception as e:
                info = f"Error: {str(e)}"
        else:
            info = "Please drop a valid image file."

        if not self.dialog:
            self.dialog = MDDialog(
                title='Info',
                text=info,
                buttons=[MDFlatButton(text='CLOSE', on_release=self.close_dialog)]
            )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss(force=True)


if __name__ == '__main__':
    RemoveMetadataApp().run()

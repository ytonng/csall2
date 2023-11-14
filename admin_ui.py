from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QPushButton, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap, QImage
import mysql.connector
import base64
from functools import partial


def connect_to_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="desmond1234",
        database="tourism information kiosk"
    )
    if connection.is_connected():
        return connection


def close_database_connection(connection):
    connection.close()


def fetch_data_from_database(connection):
    if connection:
        try:
            cursor = connection.cursor()
            query = """
            SELECT a.attractions_id, a.attractions_name, a.attractions_price, a.description, a.attractions_address, i.image_data, c.category_name
            FROM attractions AS a
            LEFT JOIN image AS i ON a.attractions_id = i.attractions_id
            LEFT JOIN category AS c ON a.category_id = c.category_id
            """
            cursor.execute(query)
            data = cursor.fetchall()
            return data
        except Exception as e:
            print(f"Error fetching data from the database: {str(e)}")
            return None
    else:
        print("No database connection established.")
        return None


def update_data_to_database(attractions_id, attractions_name, attractions_price, attractions_address, description,
                            category_name):
    # Establish a database connection
    db_connection = connect_to_database()

    if db_connection:
        # Create a cursor
        cursor = db_connection.cursor()

        try:
            # Retrieve the category_id based on the category_name
            cursor.execute("SELECT category_id FROM category WHERE category_name = %s", (category_name,))
            category_id = cursor.fetchone()[0]  # Get the category_id

            # Update the "attractions" table, including the category ID
            update_attractions_query = """
            UPDATE attractions
            SET attractions_name = %s, attractions_price = %s, attractions_address = %s, description = %s, category_id = %s
            WHERE attractions_id = %s
            """
            cursor.execute(update_attractions_query,
                           (attractions_name, attractions_price, attractions_address, description, category_id,
                            attractions_id))

            # Commit the changes to the database
            db_connection.commit()

        except Exception as e:
            print(f"Error updating data: {str(e)}")
            db_connection.rollback()  # Rollback changes in case of an error

        # Close the cursor and the database connection
        cursor.close()
        db_connection.close()


def update_deals_to_database(deals_id, deals_name, deals_description, promocode, discount, attractions_id):
    # Establish a database connection
    db_connection = connect_to_database()

    if db_connection:
        # Create a cursor
        cursor = db_connection.cursor()

        # Define the SQL statement to update the data for the 'deals' table
        update_query = """
        UPDATE deals
        SET deals_name = %s, deals_description = %s, promocode = %s,discount = %s,  attractions_id = %s
        WHERE deals_id = %s
        """

        # Execute the SQL query with the updated data
        cursor.execute(update_query,
                       (deals_name, deals_description, promocode, discount, attractions_id, deals_id))

        # Commit the changes to the database
        db_connection.commit()

        # Close the cursor and the database connection
        cursor.close()
        db_connection.close()


def update_image_in_database(deals_id, image_data):
    # Establish a database connection
    db_connection = connect_to_database()

    if db_connection:
        # Create a cursor
        cursor = db_connection.cursor()

        # Check if there is already an image record for the given deals_id
        cursor.execute("SELECT * FROM image WHERE deals_id = %s", (deals_id,))
        existing_image = cursor.fetchone()

        if existing_image:
            existing_image_data = existing_image[1]  # Assuming image_data is the second column
            # Check if the image data has changed
            if existing_image_data != image_data:
                # If the image data has changed, update the image_data
                update_image_query = """
                UPDATE image
                SET image_data = %s
                WHERE deals_id = %s
                """
                cursor.execute(update_image_query, (image_data, deals_id))
        else:
            # If no image record exists, insert a new record
            insert_image_query = """
            INSERT INTO image (deals_id, image_data) VALUES (%s, %s)
            """
            cursor.execute(insert_image_query, (deals_id, image_data))

        # Commit the changes to the database
        db_connection.commit()

        # Close the cursor and the database connection
        cursor.close()
        db_connection.close()


def update_attractions_image_in_database(attractions_id, image_data):
    # Establish a database connection
    db_connection = connect_to_database()

    if db_connection:
        # Create a cursor
        cursor = db_connection.cursor()

        # Check if there is already an image record for the given attractions_id
        cursor.execute("SELECT * FROM image WHERE attractions_id = %s", (attractions_id,))
        existing_image = cursor.fetchone()

        if existing_image:
            existing_image_data = existing_image[1]  # Assuming image_data is the second column
            # Check if the image data has changed
            if existing_image_data != image_data:
                # If the image data has changed, update the image_data
                update_image_query = """
                UPDATE image
                SET image_data = %s
                WHERE attractions_id = %s
                """
                cursor.execute(update_image_query, (image_data, attractions_id))
        else:
            # If no image record exists, insert a new record
            insert_image_query = """
            INSERT INTO image (attractions_id, image_data) VALUES (%s, %s)
            """
            cursor.execute(insert_image_query, (attractions_id, image_data))

        # Commit the changes to the database
        db_connection.commit()

        # Close the cursor and the database connection
        cursor.close()
        db_connection.close()


def fetch_category_id_from_database(category_name):
    cursor = db_connection.cursor()
    cursor.execute("SELECT category_id FROM category WHERE category_name = %s", (category_name,))
    category_id = cursor.fetchone()
    cursor.close()
    if category_id:
        return category_id[0]
    return None


def fetch_options_from_database(db_connection):
    options = []

    # Create a cursor
    cursor = db_connection.cursor()

    # Define your SQL query to fetch options from another table
    options_query = "SELECT category_name FROM category"

    # Execute the query
    cursor.execute(options_query)

    # Fetch all the options
    options_data = cursor.fetchall()

    # If there are options, extract them
    if options_data:
        options = [str(option[0]) for option in options_data]

    # Close the cursor
    cursor.close()

    return options


class Ui_MainWindow(object):
    def save_data_from_frame_to_database(self, new_frame):
        try:
            # Get the data from the widgets in the new frame
            text_edit2 = new_frame.findChild(QtWidgets.QTextEdit, "text_edit2")
            text_to_save_text_edit2 = text_edit2.toPlainText()

            text_edit_3 = new_frame.findChild(QtWidgets.QTextEdit, "text_edit_3")
            text_to_save_text_edit_3 = text_edit_3.toPlainText()

            text_edit_4 = new_frame.findChild(QtWidgets.QTextEdit, "text_edit_4")
            text_to_save_text_edit_4 = text_edit_4.toPlainText()

            small_text_edit = new_frame.findChild(QtWidgets.QTextEdit, "small_text_edit")
            text_to_save_small_text_edit = small_text_edit.toPlainText()

            # Establish a database connection
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="desmond1234",
                database="tourism information kiosk"
            )
            cursor = db_connection.cursor()

            # Insert the data into the database (modify this as needed)
            insert_data_sql = "INSERT INTO deals(deals_name, discount, promocode, attractions_id) VALUES (%s, %s, %s, %s)"
            data_params = (
                text_to_save_text_edit2, text_to_save_text_edit_3, text_to_save_text_edit_4,
                text_to_save_small_text_edit)
            cursor.execute(insert_data_sql, data_params)

            # Get the last inserted attractions_id
            deals_id = cursor.lastrowid

            # Insert the image data into the image table
            image_label = self.stackedWidget.currentWidget().findChild(QtWidgets.QLabel, "image_label")
            image_pixmap = image_label.pixmap()  # Get the QPixmap from the QLabel

            # Convert QPixmap to bytes
            image_byte_array = QtCore.QByteArray()
            buffer = QtCore.QBuffer(image_byte_array)
            buffer.open(QtCore.QIODevice.WriteOnly)
            image_pixmap.save(buffer, "PNG")  # You can change the format as needed

            # Convert QByteArray to Python bytearray
            image_data = bytes(image_byte_array)

            insert_image_sql = "INSERT INTO image (image_name, deals_id, image_data) VALUES (%s, %s, %s)"
            image_params = (text_to_save_text_edit2, deals_id, image_data)
            cursor.execute(insert_image_sql, image_params)

            db_connection.commit()

            # Close the cursor and database connection
            cursor.close()
            db_connection.close()

            # Optionally, show a message to indicate that the data has been saved
            QtWidgets.QMessageBox.information(None, "Information", "Data has been saved to the database.")
        except Exception as e:
            # Handle any exceptions that might occur, e.g., database connection issues
            QtWidgets.QMessageBox.critical(None, "Error", f"An error occurred: {str(e)}")

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def fetch_data_from_database(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="desmond1234",
                database="tourism information kiosk"
            )
            cursor = connection.cursor()
            cursor.execute("""
                SELECT d.deals_id, deals_name,d.deals_description,d.discount, d.promocode, d.attractions_id, i.image_data
            FROM deals AS d
            LEFT JOIN image AS i ON d.deals_id = i.deals_id
            """)
            data = cursor.fetchall()
            cursor.close()
            connection.close()
            return data
        except Exception as e:
            print(f"Error fetching data from database: {str(e)}")

    def create_display_deals_frame(self):
        # Clear existing widgets in the layout
        self.clear_layout(self.verticalLayout_6)
        data = self.fetch_data_from_database()
        frames = []  # Create a list to store the created frames

        if data:
            for index, (
                    deals_id, deals_name, deals_description, discount, promocode, attractions_id,
                    image_data) in enumerate(data):

                newframe = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
                newframe.setFixedSize(1200, 500)  # Adjust the size of the new frame
                newframe.setFrameShape(QtWidgets.QFrame.Box)
                newframe.setFrameShadow(QtWidgets.QFrame.Raised)
                newframe.setObjectName("newframe")
                # Add the new frame to the vertical layout inside the deals page (scroll area) at the top
                self.verticalLayout_6.insertWidget(0, newframe)  # Insert at the beginning of the layout
                imagelabel = QLabel(newframe)
                imagelabel.setGeometry(QtCore.QRect(20, 20, 400, 500))  # Adjust the position and size as needed
                imagelabel.setObjectName("imagelabel")
                # Convert binary image_data to QImage
                image = QImage()
                image.loadFromData(image_data)  # Load image from binary data
                # Create QPixmap from the QImage
                pixmap = QPixmap.fromImage(image)
                # Set the pixmap to the QLabel
                imagelabel.setPixmap(pixmap)
                imagelabel.setScaledContents(True)
                imagelabel.setAlignment(QtCore.Qt.AlignCenter)

                textedit2 = QtWidgets.QTextEdit(newframe)
                textedit2.setGeometry(
                    QtCore.QRect(600, 20, 600, 50))  # Position the first text edit to the right of the label
                textedit2.setPlainText(deals_name)  # Set the text for text_edit2
                textedit2.setObjectName("textedit2")
                textedit2.setReadOnly(True)  # Assuming text_edit2 is for displaying data

                inputframe_3 = QtWidgets.QFrame(newframe)
                inputframe_3.setGeometry(QtCore.QRect(600, 80, 600, 250))  # Adjust the position and size as needed
                inputframe_3.setFrameShape(QtWidgets.QFrame.Box)
                inputframe_3.setFrameShadow(QtWidgets.QFrame.Raised)
                inputframe_3.setObjectName("input_frame_3")

                textedit_3 = QtWidgets.QTextEdit(inputframe_3)
                textedit_3.setGeometry(QtCore.QRect(10, 10, 580, 200))  # Adjust the position and size
                textedit_3.setPlainText(
                    deals_description)  # Convert discount to string and set the text for text_edit_3
                textedit_3.setObjectName("textedit_3")
                textedit_3.setReadOnly(True)  # Assuming text_edit_3 is for displaying data

                inputframe_4 = QtWidgets.QFrame(newframe)
                inputframe_4.setGeometry(QtCore.QRect(600, 300, 600, 200))  # Adjust the position and size as needed
                inputframe_4.setFrameShape(QtWidgets.QFrame.Box)
                inputframe_4.setFrameShadow(QtWidgets.QFrame.Raised)
                inputframe_4.setObjectName("inputframe_4")

                textedit_4 = QtWidgets.QTextEdit(inputframe_4)
                textedit_4.setGeometry(QtCore.QRect(10, 10, 580, 100))  # Adjust the position and size
                textedit_4.setPlainText(promocode)  # Set the text for text_edit_4
                textedit_4.setObjectName("textedit_4")
                textedit_4.setReadOnly(True)  # Assuming text_edit_4 is for displaying data

                newtext_edit = QtWidgets.QTextEdit(newframe)
                newtext_edit.setGeometry(QtCore.QRect(450, 100, 150, 50))  # Set the geometry as specified
                newtext_edit.setPlainText(str(deals_id))  # Convert deals_id to string and set the initial text
                newtext_edit.setObjectName("newtext_edit")

                new_text_edit_2 = QtWidgets.QTextEdit(newframe)
                new_text_edit_2.setGeometry(QtCore.QRect(450, 160, 150, 50))  # Set the geometry as desired
                new_text_edit_2.setPlainText(str(attractions_id))  # Set the initial text (you can change this)
                new_text_edit_2.setObjectName("new_text_edit_2")  # Give it a unique object name

                edit_button = QPushButton("Edit", newframe)
                edit_button.setGeometry(QtCore.QRect(450, 20, 150, 30))
                # Store the attractions_id as a property of the button for reference
                edit_button.deals_id = deals_id
                upload_button = QPushButton(newframe)
                upload_button.setGeometry(QtCore.QRect(450, 220, 150, 30))  # Adjust the button position and size
                upload_button.setObjectName("upload_button")
                upload_button.setText("Upload")
                upload_button.setVisible(False)

                def toggle_edit_save():
                    if edit_button.text() == "Edit":
                        edit_button.setText("Save")
                        # Enable input widgets for editing
                        textedit2.setReadOnly(False)
                        textedit_3.setReadOnly(False)
                        textedit_4.setReadOnly(False)
                        smalltext_edit.setReadOnly(False)
                        newtext_edit.setReadOnly(False)
                        new_text_edit_2.setReadOnly(False)
                        upload_button.setVisible(True)
                    elif edit_button.text() == "Save":
                        edit_button.setText("Edit")
                        # Disable input widgets after saving
                        textedit2.setReadOnly(True)
                        textedit_3.setReadOnly(True)
                        textedit_4.setReadOnly(True)
                        smalltext_edit.setReadOnly(True)
                        new_text_edit_2.setReadOnly(True)
                        upload_button.setVisible(False)
                        # Get updated data from widgets
                        deals_name = textedit2.toPlainText()
                        deals_description = textedit_3.toPlainText()
                        promocode = textedit_4.toPlainText()
                        discount = smalltext_edit.toPlainText()
                        attractions_id = int(new_text_edit_2.toPlainText())
                        update_deals_to_database(deals_id, deals_name, deals_description, promocode, discount,
                                                 attractions_id)
                        update_image_in_database(deals_id, image_data)

                edit_button.clicked.connect(toggle_edit_save)

                smalltext_edit = QtWidgets.QTextEdit(newframe)
                smalltext_edit.setGeometry(
                    QtCore.QRect(textedit2.x() + textedit2.width() - 104, textedit2.y(), 104,
                                 51))  # Adjust the height as needed
                smalltext_edit.setPlainText(
                    str(discount))  # Convert attractions_id to string and set the text for the small text edit
                smalltext_edit.setObjectName("smalltext_edit")
                smalltext_edit.setReadOnly(True)  # Assuming small_text_edit is for displaying data

                # Create a "Clear" button for clearing the frame
                clear_button = QPushButton("Clear", newframe)
                clear_button.setGeometry(QtCore.QRect(450, 60, 150, 30))
                clear_button.clicked.connect(
                    lambda _, frame=newframe, deals_id=deals_id, attractions_id=None: self.clear_frame(frame, deals_id,
                                                                                                       attractions_id))

                # Create an "Upload" button for updating the image
                upload_button.clicked.connect(lambda _, frame=newframe: self.deals_upload_image(frame, deals_id))
                upload_button.setVisible(False)

                frames.append(newframe)  # Append the frame to the list of frames

        return frames  # Return the list of frames outside the for loop
        db_connection.close()

    def deals_upload_image(self, frame, deals_id):
        # Open a file dialog to get the path of the new image
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg)")

        if file_path:
            # Read the new image data
            with open(file_path, "rb") as image_file:
                image_data = image_file.read()

            # Update the image_data in the database
            update_image_in_database(deals_id, image_data)

            # Update the displayed image in the frame
            imagelabel = frame.findChild(QtWidgets.QLabel, "imagelabel")
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            imagelabel.setPixmap(pixmap)
            imagelabel.setScaledContents(True)
            imagelabel.setAlignment(QtCore.Qt.AlignCenter)

            # Optionally, show a message to indicate that the image has been updated
            QtWidgets.QMessageBox.information(None, "Information", "Image has been updated.")

    def add_new_frame_to_dealspage(self):
        # Create a new frame
        new_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        new_frame.setFixedSize(1200, 500)  # Set the size of the new frame
        new_frame.setFrameShape(QtWidgets.QFrame.Box)
        new_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        new_frame.setObjectName("new_frame")

        # Add the new frame to the vertical layout inside the dealspage (scroll area) at the top
        self.verticalLayout_6.insertWidget(0, new_frame)

        image_label = QLabel(new_frame)
        image_label.setGeometry(QtCore.QRect(20, 20, 400, 500))  # Adjust the position and size as needed
        image_label.setObjectName("image_label")

        # Create a button for uploading an image
        upload_button = QPushButton("Upload Image", new_frame)
        upload_button.setGeometry(QtCore.QRect(450, 20, 150, 30))  # Adjust the button position and size
        upload_button.setObjectName("upload_button")

        # Create a button to clear the frame
        clear_button = QPushButton("Clear", new_frame)
        clear_button.setGeometry(QtCore.QRect(450, 60, 150, 30))  # Adjust the button position and size
        clear_button.setObjectName("clear_button")

        # Create a new QTextEdit widget
        new_text_edit = QtWidgets.QTextEdit(new_frame)
        new_text_edit.setGeometry(QtCore.QRect(450, 100, 150, 50))  # Set the geometry as specified
        new_text_edit.setPlainText("New Text Here")  # Set the initial text (you can change this)
        new_text_edit.setObjectName("new_text_edit")  # Give it a unique object name

        new_text_edit_2 = QtWidgets.QTextEdit(new_frame)
        new_text_edit_2.setGeometry(QtCore.QRect(450, 160, 150, 50))  # Set the geometry as desired
        new_text_edit_2.setPlainText("New Text Here 2")  # Set the initial text (you can change this)
        new_text_edit_2.setObjectName("new_text_edit_2")  # Give it a unique object name

        # Optionally, configure the new QTextEdit as needed.
        new_text_edit_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        # Remove the frame for the new QTextEdit
        new_text_edit.setFrameShape(QtWidgets.QFrame.NoFrame)

        # Connect the upload button to the function that allows image upload
        upload_button.clicked.connect(lambda: self.open_image_dialog(image_label))

        clear_button.clicked.connect(
            lambda _, frame=new_frame, deals_id=deals_id, attractions_id=attractions_id: self.clear_frame(frame,
                                                                                                          deals_id,
                                                                                                          attractions_id))

        # Optionally, configure the QLabel as needed.
        image_label.setScaledContents(True)
        image_label.setAlignment(QtCore.Qt.AlignCenter)

        # Add a QTextEdit widget to the new frame (text_edit2 remains the same)
        text_edit2 = QtWidgets.QTextEdit(new_frame)
        text_edit2.setGeometry(
            QtCore.QRect(600, 20, 600, 50))  # Position the first text edit to the right of the label
        text_edit2.setPlainText("Your Text Here 2")  # Set the text for the first text edit
        text_edit2.setObjectName("text_edit2")

        # Set font for text_edit2
        font_text_edit2 = QtGui.QFont()
        font_text_edit2.setPointSize(12)  # Set the point size to 12
        font_text_edit2.setBold(True)  # Set the font to bold
        text_edit2.setFont(font_text_edit2)

        input_frame_3 = QtWidgets.QFrame(new_frame)
        input_frame_3.setGeometry(QtCore.QRect(600, 80, 600, 250))  # Adjust the position and size as needed
        input_frame_3.setFrameShape(QtWidgets.QFrame.Box)
        input_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        input_frame_3.setObjectName("input_frame_3")

        # Create a QTextEdit for input text 3
        text_edit_3 = QtWidgets.QTextEdit(input_frame_3)
        text_edit_3.setGeometry(QtCore.QRect(10, 10, 580, 200))  # Adjust the position and size
        text_edit_3.setPlainText("Your Text Here 3")  # Set the initial text
        text_edit_3.setObjectName("text_edit_3")
        text_edit_3.setFrameShape(QtWidgets.QFrame.Panel)
        text_edit_3.setFrameShadow(QtWidgets.QFrame.Raised)

        # Set font for text_edit_3
        font_text_edit_3 = QtGui.QFont()
        font_text_edit_3.setPointSize(11)  # Set the point size to 11
        text_edit_3.setFont(font_text_edit_3)

        input_frame_4 = QtWidgets.QFrame(new_frame)
        input_frame_4.setGeometry(QtCore.QRect(600, 300, 600, 200))  # Adjust the position and size as needed
        input_frame_4.setFrameShape(QtWidgets.QFrame.Box)
        input_frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        input_frame_4.setObjectName("input_frame_4")

        # Create a QTextEdit for input text 4
        text_edit_4 = QtWidgets.QTextEdit(input_frame_4)
        text_edit_4.setGeometry(QtCore.QRect(10, 10, 580, 100))  # Adjust the position and size
        text_edit_4.setPlainText("Your Text Here 4")  # Set the initial text
        text_edit_4.setObjectName("text_edit_4")
        text_edit_4.setFrameShape(QtWidgets.QFrame.Panel)
        text_edit_4.setFrameShadow(QtWidgets.QFrame.Raised)

        # Set font for text_edit_4
        font_text_edit_4 = QtGui.QFont()
        font_text_edit_4.setPointSize(11)  # Set the point size to 11
        text_edit_4.setFont(font_text_edit_4)

        # Set a frame shadow for text_edit2
        text_edit2.setFrameShape(QtWidgets.QFrame.Panel)
        text_edit2.setFrameShadow(QtWidgets.QFrame.Raised)

        # Add a small QTextEdit to the new frame (top-right side of text_edit2)
        small_text_edit = QtWidgets.QTextEdit(new_frame)
        small_text_edit.setGeometry(
            QtCore.QRect(text_edit2.x() + text_edit2.width() - 104, text_edit2.y(), 104,
                         51))  # Adjust the height as needed
        small_text_edit.setPlainText("Small Text Here")  # Set the text for the small text edit
        small_text_edit.setObjectName("small_text_edit")

        # Set font for small_text_edit
        font_small_text_edit = QtGui.QFont()
        font_small_text_edit.setPointSize(12)  # Set the point size to 12
        font_small_text_edit.setBold(True)  # Make the font bold
        small_text_edit.setFont(font_small_text_edit)

        # Optionally, configure the text edit (text_edit2), small text edit, and label as needed.
        text_edit2.setReadOnly(False)
        small_text_edit.setReadOnly(False)
        self.save_deals_button.clicked.connect(lambda: self.save_data_from_frame_to_database(new_frame))

    def save_attractions_data_from_frame_to_database(self, new_frame):
        try:
            # Get the text from text_edit2
            text_edit2 = new_frame.findChild(QtWidgets.QTextEdit, "text_edit2")
            text_to_save_text_edit2 = text_edit2.toPlainText()

            # Get the text from small_text_edit
            small_text_edit = new_frame.findChild(QtWidgets.QTextEdit, "small_text_edit")
            text_to_save_small_text_edit = small_text_edit.toPlainText()

            # Get the text from text_edit_3
            text_edit_3 = new_frame.findChild(QtWidgets.QTextEdit, "text_edit_3")
            text_to_save_text_edit3 = text_edit_3.toPlainText()

            # Get the text from text_edit_4
            text_edit_4 = new_frame.findChild(QtWidgets.QTextEdit, "text_edit_4")
            text_to_save_text_edit4 = text_edit_4.toPlainText()

            # Get the category_name from the input_widget (ComboBox)
            input_widget = new_frame.findChild(QtWidgets.QComboBox, "input_widget")
            category_name = input_widget.currentText()

            # Establish a database connection
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="desmond1234",
                database="tourism information kiosk"
            )
            cursor = db_connection.cursor()

            # Retrieve the category_id based on category_name
            cursor.execute("SELECT category_id FROM category WHERE category_name = %s", (category_name,))
            category_id = cursor.fetchone()[0]

            # Insert the data into the attractions table
            insert_attractions_sql = "INSERT INTO attractions (attractions_name, description, attractions_address, attractions_price, category_id) VALUES (%s, %s, %s, %s, %s)"
            attractions_params = (
                text_to_save_text_edit2, text_to_save_text_edit3, text_to_save_text_edit4, text_to_save_small_text_edit,
                category_id)
            cursor.execute(insert_attractions_sql, attractions_params)

            # Get the last inserted attractions_id
            attractions_id = cursor.lastrowid

            image_label = self.stackedWidget.currentWidget().findChild(QtWidgets.QLabel, "image_label")
            image_pixmap = image_label.pixmap()  # Get the QPixmap from the QLabel

            # Convert QPixmap to bytes
            image_byte_array = QtCore.QByteArray()
            buffer = QtCore.QBuffer(image_byte_array)
            buffer.open(QtCore.QIODevice.WriteOnly)
            image_pixmap.save(buffer, "PNG")  # You can change the format as needed

            # Convert QByteArray to Python bytearray
            image_data = bytes(image_byte_array)

            insert_image_sql = "INSERT INTO image (image_name, attractions_id, image_data) VALUES (%s, %s, %s)"
            image_params = (text_to_save_text_edit2, attractions_id, image_data)
            cursor.execute(insert_image_sql, image_params)

            db_connection.commit()

            db_connection.close()

            # Optionally, show a message to indicate that the data has been saved
            QtWidgets.QMessageBox.information(None, "Information", "Data has been saved to the database.")
        except Exception as e:
            # Handle any exceptions that might occur, e.g., database connection issues
            QtWidgets.QMessageBox.critical(None, "Error", f"An error occurred: {str(e)}")

    def display_attractions_data(self):
        # Clear existing widgets in the layout
        self.clear_layout(self.verticalLayout_10)
        # Establish a database connection
        db_connection = connect_to_database()

        if db_connection:
            # Fetch data from the 'attractions' table
            data = fetch_data_from_database(db_connection)

            if data:
                # You have your data, now display it in your widgets
                frames = []  # Create a list to store the created frames

                for index, (
                        attractions_id, attractions_name, description, attractions_address, attractions_price,
                        image_data,
                        category_name) in enumerate(data):

                    new_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
                    new_frame.setFixedSize(1200, 500)
                    new_frame.setFrameShape(QtWidgets.QFrame.Box)
                    new_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                    new_frame.setObjectName("new_frame")

                    # Add the new frame to your layout, assuming you have a layout in your widget
                    self.verticalLayout_10.insertWidget(0, new_frame)

                    imagelabel = QLabel(new_frame)
                    imagelabel.setGeometry(QtCore.QRect(20, 20, 400, 500))
                    imagelabel.setObjectName("imagelabel")

                    input_widget = QtWidgets.QComboBox(new_frame)
                    input_widget.setObjectName("input_widget")
                    input_widget.setEditable(True)
                    input_widget.setGeometry(QtCore.QRect(450, 150, 150, 30))

                    # Fetch options data from the 'options' table
                    options = fetch_options_from_database(db_connection)

                    # Populate the QComboBox with options
                    for option in options:
                        input_widget.addItem(option)

                    # Set the correct category for this attraction
                    input_widget.setCurrentText(category_name)

                    # Disable the combo box by default
                    input_widget.setDisabled(True)

                    # Set the image for image_label
                    image = QImage()
                    image.loadFromData(image_data)
                    pixmap = QPixmap.fromImage(image)
                    imagelabel.setPixmap(pixmap)
                    imagelabel.setScaledContents(True)
                    imagelabel.setAlignment(QtCore.Qt.AlignCenter)

                    # Set text for your other widgets (labels, text edits, etc.)
                    textedit2 = QtWidgets.QTextEdit(new_frame)
                    textedit2.setGeometry(QtCore.QRect(600, 20, 600, 50))
                    textedit2.setPlainText(attractions_name)
                    textedit2.setObjectName("textedit2")
                    textedit2.setReadOnly(True)

                    # Create a new frame for input text (frame 3)
                    input_frame_3 = QtWidgets.QFrame(new_frame)
                    input_frame_3.setGeometry(QtCore.QRect(600, 80, 600, 250))

                    # Create a QTextEdit for input text 3
                    textedit_3 = QtWidgets.QTextEdit(input_frame_3)
                    textedit_3.setGeometry(QtCore.QRect(10, 10, 580, 200))
                    textedit_3.setPlainText(str(attractions_price))
                    textedit_3.setObjectName("textedit_3")
                    textedit_3.setFrameShape(QtWidgets.QFrame.Panel)
                    textedit_3.setFrameShadow(QtWidgets.QFrame.Raised)

                    # Create a new frame for input text (frame 4)
                    input_frame_4 = QtWidgets.QFrame(new_frame)
                    input_frame_4.setGeometry(QtCore.QRect(600, 300, 600, 200))

                    # Create a new QTextEdit for the new input field without a frame
                    newtext_edit = QtWidgets.QTextEdit(new_frame)
                    newtext_edit.setGeometry(QtCore.QRect(450, 100, 150, 50))
                    newtext_edit.setPlainText(str(attractions_id))
                    newtext_edit.setObjectName("newtext_edit")
                    newtext_edit.setFrameShape(QtWidgets.QFrame.NoFrame)

                    # Create a QTextEdit for input text 4
                    textedit_4 = QtWidgets.QTextEdit(input_frame_4)
                    textedit_4.setGeometry(QtCore.QRect(10, 10, 580, 100))
                    textedit_4.setPlainText(attractions_address)
                    textedit_4.setObjectName("text_edit_4")
                    textedit_4.setFrameShape(QtWidgets.QFrame.Panel)
                    textedit_4.setFrameShadow(QtWidgets.QFrame.Raised)

                    # Add a small QTextEdit to the new frame (top-right side of text_edit2)
                    smalltext_edit = QtWidgets.QTextEdit(new_frame)
                    smalltext_edit.setGeometry(
                        QtCore.QRect(textedit2.x() + textedit2.width() - 104, textedit2.y(), 104, 51))
                    smalltext_edit.setPlainText(str(description))
                    smalltext_edit.setObjectName("small_text_edit")
                    smalltext_edit.setFrameShape(QtWidgets.QFrame.Panel)
                    smalltext_edit.setFrameShadow(QtWidgets.QFrame.Raised)

                    # Store attractions_id as an attribute of the new_frame
                    new_frame.attractions_id = attractions_id

                    clear_button = QPushButton("Clear", new_frame)
                    clear_button.setGeometry(QtCore.QRect(450, 60, 150, 30))
                    clear_button.clicked.connect(
                        lambda _, frame=new_frame, deals_id=None, attractions_id=attractions_id: self.clear_frame(frame,
                                                                                                                  deals_id,
                                                                                                                  attractions_id)
                    )

                    # Optionally, configure the QLabel as needed.
                    imagelabel.setScaledContents(True)
                    imagelabel.setAlignment(QtCore.Qt.AlignCenter)
                    smalltext_edit.setFrameShape(QtWidgets.QFrame.Panel)
                    smalltext_edit.setFrameShadow(QtWidgets.QFrame.Raised)

                    edit_button = QPushButton("Edit", new_frame)
                    edit_button.setGeometry(QtCore.QRect(450, 20, 150, 30))
                    # Store the attractions_id as a property of the button for reference
                    edit_button.attractions_id = attractions_id

                    # Connect the edit_button_clicked signal to the handle_edit function
                    edit_button.clicked.connect(
                        lambda _, button=edit_button, frame=new_frame, id=attractions_id,
                               image_data=image_data: self.handle_edit(id, button, frame, image_data)
                    )

                    upload_button = QPushButton(new_frame)
                    upload_button.setGeometry(QtCore.QRect(450, 220, 150, 30))
                    upload_button.setObjectName("upload_button")
                    upload_button.setText("Upload")
                    upload_button.setVisible(False)

                    # Optionally, connect the upload_button_clicked signal if needed
                    upload_button.clicked.connect(
                        partial(self.upload_image, frame=new_frame, attractions_id=attractions_id))
                    upload_button.setVisible(False)

                    frames.append(new_frame)
                return frames
            db_connection.close()

    def handle_edit(self, attractions_id, button, frame, image_data):
        if button.text() == "Edit":
            button.setText("Save")
            # Enable input widgets for editing
            frame.findChild(QtWidgets.QTextEdit, "textedit2").setReadOnly(False)
            frame.findChild(QtWidgets.QTextEdit, "textedit_3").setReadOnly(False)
            frame.findChild(QtWidgets.QTextEdit, "text_edit_4").setReadOnly(False)
            frame.findChild(QtWidgets.QTextEdit, "small_text_edit").setReadOnly(False)
            frame.findChild(QtWidgets.QComboBox, "input_widget").setDisabled(False)  # Enable the combo box for editing
            frame.findChild(QPushButton, "upload_button").setVisible(True)
        elif button.text() == "Save":
            button.setText("Edit")
            # Disable input widgets after saving
            frame.findChild(QtWidgets.QTextEdit, "textedit2").setReadOnly(True)
            frame.findChild(QtWidgets.QTextEdit, "textedit_3").setReadOnly(True)
            frame.findChild(QtWidgets.QTextEdit, "text_edit_4").setReadOnly(True)
            frame.findChild(QtWidgets.QTextEdit, "small_text_edit").setReadOnly(True)
            frame.findChild(QtWidgets.QComboBox, "input_widget").setDisabled(True)  # Make the combo box read-only again
            frame.findChild(QPushButton, "upload_button").setVisible(False)

            # Get updated data from widgets
            attractions_id = int(frame.findChild(QtWidgets.QTextEdit, "newtext_edit").toPlainText())
            attractions_name = frame.findChild(QtWidgets.QTextEdit, "textedit2").toPlainText()
            attractions_address = frame.findChild(QtWidgets.QTextEdit, "textedit_3").toPlainText()
            description = frame.findChild(QtWidgets.QTextEdit, "text_edit_4").toPlainText()
            attractions_price = float(frame.findChild(QtWidgets.QTextEdit, "small_text_edit").toPlainText())
            category = frame.findChild(QtWidgets.QComboBox,
                                       "input_widget").currentText()  # Get the selected category from the QComboBox

            # Save the updated data to the database
            update_data_to_database(attractions_id, attractions_name, attractions_price, attractions_address,
                                    description, category)
            # Update the image data in the database
            update_attractions_image_in_database(attractions_id, image_data)

    def upload_image(self, frame, attractions_id):
        # Get the file path from a file dialog or any other means
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg)")

        if file_path:
            # Read the image file
            with open(file_path, 'rb') as file:
                image_data = file.read()

            update_attractions_image_in_database(attractions_id, image_data)

            # Update the QLabel with the new image
            imagelabel = frame.findChild(QtWidgets.QLabel, "imagelabel")
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            imagelabel.setPixmap(pixmap)
            imagelabel.setScaledContents(True)
            imagelabel.setAlignment(QtCore.Qt.AlignCenter)

            # Optionally, show a message to indicate that the image has been updated
            QtWidgets.QMessageBox.information(None, "Information", "Image has been updated.")

    def clear_frame(self, frame, deals_id, attractions_id):
        # Remove the widgets from the frame
        for widget in frame.findChildren(QtWidgets.QWidget):
            widget.deleteLater()

        # Call your method to delete data from the database
        self.delete_deals_data_from_database(deals_id)
        self.delete_attractions_data_from_database(attractions_id)

        # Remove the frame from the layout
        self.verticalLayout_6.removeWidget(frame)
        frame.deleteLater()

    def delete_deals_data_from_database(self, deals_id):
        # Replace this with your database interaction code to delete data based on deals_id
        db_connection = connect_to_database()
        if db_connection:
            cursor = db_connection.cursor()

            delete_attractions_query = "DELETE FROM image WHERE deals_id = %s"
            cursor.execute(delete_attractions_query, (deals_id,))

            delete_deals_query = "DELETE FROM deals WHERE deals_id = %s"
            cursor.execute(delete_deals_query, (deals_id,))

            db_connection.commit()
            db_connection.close()

    def delete_attractions_data_from_database(self, attractions_id):
        # Replace this with your database interaction code to delete data based on attractions_id
        db_connection = connect_to_database()
        if db_connection:
            cursor = db_connection.cursor()

            # 1. Delete image_data from the image table
            delete_image_data_query = "DELETE FROM image WHERE attractions_id = %s"
            cursor.execute(delete_image_data_query, (attractions_id,))

            # 2. Delete the corresponding entry from the attractions table
            delete_attractions_query = "DELETE FROM attractions WHERE attractions_id = %s"
            cursor.execute(delete_attractions_query, (attractions_id,))

            db_connection.commit()
            db_connection.close()

    def open_image_dialog(self, label):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_name, _ = QFileDialog.getOpenFileName(None, "Open Image File", "",
                                                   "Image Files (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)",
                                                   options=options)
        if file_name:
            self.display_image(label, file_name)

    def display_image(self, label, file_name):
        pixmap = QPixmap(file_name)
        label.setPixmap(pixmap.scaled(label.size(), QtCore.Qt.KeepAspectRatio))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1308, 718)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_label_1 = QtWidgets.QLabel(self.icon_only_widget)
        self.logo_label_1.setMinimumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setMaximumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setStyleSheet("")
        self.logo_label_1.setText("")
        self.logo_label_1.setScaledContents(True)
        self.logo_label_1.setObjectName("logo_label_1")
        self.horizontalLayout_3.addWidget(self.logo_label_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 30, -1, 0)
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setObjectName("verticalLayout")
        self.attraction_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.attraction_btn_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("attraction.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.attraction_btn_1.setIcon(icon)
        self.attraction_btn_1.setCheckable(True)
        self.attraction_btn_1.setAutoExclusive(True)
        self.attraction_btn_1.setObjectName("attraction_btn_1")
        self.verticalLayout.addWidget(self.attraction_btn_1)
        self.deals_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.deals_btn_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("deal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deals_btn_1.setIcon(icon1)
        self.deals_btn_1.setCheckable(True)
        self.deals_btn_1.setAutoExclusive(True)
        self.deals_btn_1.setObjectName("deals_btn_1")
        self.verticalLayout.addWidget(self.deals_btn_1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 375, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.exit_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.exit_btn_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("exit1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn_1.setIcon(icon2)
        self.exit_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.exit_btn_1.setObjectName("exit_btn_1")
        self.verticalLayout_3.addWidget(self.exit_btn_1)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.full_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.full_menu_widget.setStyleSheet("gridline-color: rgb(0, 0, 0);\n"
                                            "background-color: rgb(255, 255, 255);")
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_label_2 = QtWidgets.QLabel(self.full_menu_widget)
        self.logo_label_2.setMinimumSize(QtCore.QSize(80, 40))
        self.logo_label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setText("")
        self.logo_label_2.setPixmap(QtGui.QPixmap("logo.png"))
        self.logo_label_2.setScaledContents(True)
        self.logo_label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.logo_label_2.setObjectName("logo_label_2")
        self.horizontalLayout_2.addWidget(self.logo_label_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, 30, -1, 0)
        self.verticalLayout_2.setSpacing(50)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.attraction_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(8)
        self.attraction_btn_2.setFont(font)
        self.attraction_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.attraction_btn_2.setCheckable(True)
        self.attraction_btn_2.setAutoExclusive(True)
        self.attraction_btn_2.setObjectName("attraction_btn_2")
        self.verticalLayout_2.addWidget(self.attraction_btn_2)
        self.deal_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.deal_btn_2.setFont(font)
        self.deal_btn_2.setCheckable(True)
        self.deal_btn_2.setAutoExclusive(True)
        self.deal_btn_2.setObjectName("deal_btn_2")
        self.verticalLayout_2.addWidget(self.deal_btn_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 373, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.exit_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.exit_btn_2.setFont(font)
        self.exit_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout_4.addWidget(self.exit_btn_2)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setStyleSheet("alternate-background-color: rgb(255, 255, 255);")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setStyleSheet("\n"
                                  "background-color: rgb(228, 242, 253);\n"
                                  "")
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.change_btn = QtWidgets.QPushButton(self.widget)
        self.change_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.change_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("navigationmanual.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_btn.setIcon(icon3)
        self.change_btn.setIconSize(QtCore.QSize(20, 20))
        self.change_btn.setCheckable(True)
        self.change_btn.setObjectName("change_btn")
        self.horizontalLayout_4.addWidget(self.change_btn)
        self.add_deals_button = QtWidgets.QPushButton(self.widget)
        self.add_deals_button.setObjectName("add_deals_button")
        self.horizontalLayout_4.addWidget(self.add_deals_button)
        self.save_deals_button = QtWidgets.QPushButton(self.widget)
        self.save_deals_button.setObjectName("save_deals_button")
        self.horizontalLayout_4.addWidget(self.save_deals_button)
        spacerItem2 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.add_attraction_button = QtWidgets.QPushButton(self.widget)
        self.add_attraction_button.setEnabled(True)
        self.add_attraction_button.setCheckable(False)
        self.add_attraction_button.setObjectName("add_attraction_button")
        self.horizontalLayout_4.addWidget(self.add_attraction_button)
        self.save_attraction_button = QtWidgets.QPushButton(self.widget)
        self.save_attraction_button.setEnabled(True)
        self.save_attraction_button.setCheckable(False)
        self.save_attraction_button.setObjectName("save_attraction_button")
        self.horizontalLayout_4.addWidget(self.save_attraction_button)
        self.verticalLayout_5.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_3)
        self.stackedWidget.setStyleSheet("\n"
                                         "background-color: rgb(228, 242, 253);\n"
                                         "")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_8)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.scrollArea = QtWidgets.QScrollArea(self.page_8)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1222, 3622))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_7.setMinimumSize(QtCore.QSize(1200, 3600))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_10.addWidget(self.frame_7)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_9.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_8)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_4)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1222, 3622))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bookingpage = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.bookingpage.setMinimumSize(QtCore.QSize(1200, 3600))
        self.bookingpage.setText("")
        self.bookingpage.setObjectName("bookingpage")
        self.horizontalLayout.addWidget(self.bookingpage)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.page_5)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1222, 3622))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.dealspage = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.dealspage.setMinimumSize(QtCore.QSize(1200, 3600))
        self.dealspage.setText("")
        self.dealspage.setObjectName("dealspage")
        self.verticalLayout_6.addWidget(self.dealspage)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_6.addWidget(self.scrollArea_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.change_btn.toggled['bool'].connect(self.icon_only_widget.setVisible)  # type: ignore
        self.change_btn.toggled['bool'].connect(self.full_menu_widget.setHidden)  # type: ignore
        self.exit_btn_2.clicked.connect(MainWindow.close)  # type: ignore
        self.exit_btn_1.clicked.connect(MainWindow.close)  # type: ignore
        self.deals_btn_1.toggled['bool'].connect(self.deal_btn_2.setChecked)  # type: ignore
        self.deal_btn_2.toggled['bool'].connect(self.deals_btn_1.setChecked)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.attraction_btn_2.clicked.connect(self.display_attractions_data)
        self.deal_btn_2.clicked.connect(self.create_display_deals_frame)

        button_size = QtCore.QSize(120, 50)  # Adjust the width and height as needed

        self.attraction_btn_2.setFixedSize(button_size)
        self.deal_btn_2.setFixedSize(button_size)


        button_size_1 = QtCore.QSize(75, 50)  # Adjust the width and height as needed

        self.attraction_btn_1.setFixedSize(button_size_1)
        self.deals_btn_1.setFixedSize(button_size_1)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.attraction_btn_2.setText(_translate("MainWindow", "Attraction"))
        self.deal_btn_2.setText(_translate("MainWindow", "Deals"))
        self.exit_btn_2.setText(_translate("MainWindow", "Exit"))
        self.add_deals_button.setText(_translate("MainWindow", "ADD DEALS"))
        self.save_deals_button.setText(_translate("MainWindow", "SAVE DEALS"))
        self.add_attraction_button.setText(_translate("MainWindow", "ADD ATTRACTION"))
        self.save_attraction_button.setText(_translate("MainWindow", "SAVE ATTRACTION"))

        # Add these methods to your Ui_MainWindow class
        def show_attraction_page():
            self.stackedWidget.setCurrentIndex(0)  # Change to the Attraction page

        def show_deals_page():
            self.stackedWidget.setCurrentIndex(2)  # Change to the Deals page

        # Connect buttons to their respective functions
        self.attraction_btn_2.clicked.connect(show_attraction_page)
        self.attraction_btn_1.clicked.connect(show_attraction_page)

        self.deal_btn_2.clicked.connect(show_deals_page)
        self.deals_btn_1.clicked.connect(show_deals_page)

        def add_new_frame():
            new_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
            new_frame.setFixedSize(1200, 500)  # Set the size of the new frame
            new_frame.setFrameShape(QtWidgets.QFrame.Box)
            new_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            new_frame.setObjectName("new_frame")

            # Insert the new frame at the top of the vertical layout inside the scroll area
            self.verticalLayout_10.insertWidget(0, new_frame)

            image_label = QLabel(new_frame)
            image_label.setGeometry(QtCore.QRect(20, 20, 400, 500))  # Adjust the position and size as needed
            image_label.setObjectName("image_label")

            # Create a button for uploading an image
            upload_button = QPushButton("Upload Image", new_frame)
            upload_button.setGeometry(QtCore.QRect(450, 20, 150, 30))  # Adjust the button position and size
            upload_button.setObjectName("upload_button")

            # Add the second QTextEdit to the new frame
            text_edit2 = QtWidgets.QTextEdit(new_frame)
            text_edit2.setGeometry(QtCore.QRect(600, 20, 600, 50))  # Position the second text edit below the first one
            text_edit2.setPlainText("Your Text Here 22")  # Set the text for the second text edit
            text_edit2.setObjectName("text_edit2")

            # Set font for text_edit2
            font_text_edit2 = QtGui.QFont()
            font_text_edit2.setFamily("MS Shell Dlg 2")
            font_text_edit2.setPointSize(12)
            font_text_edit2.setBold(True)  # Set the font to bold
            text_edit2.setFont(font_text_edit2)

            # Create a new frame for input text (frame 3)
            input_frame_3 = QtWidgets.QFrame(new_frame)
            input_frame_3.setGeometry(QtCore.QRect(600, 80, 600, 250))  # Adjust the position and size as needed
            input_frame_3.setFrameShape(QtWidgets.QFrame.Box)
            input_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
            input_frame_3.setObjectName("input_frame_3")

            # Create a QTextEdit for input text 3
            text_edit_3 = QtWidgets.QTextEdit(input_frame_3)
            text_edit_3.setGeometry(QtCore.QRect(10, 10, 580, 200))  # Adjust the position and size
            text_edit_3.setPlainText("Your Text Here 3")  # Set the initial text
            text_edit_3.setObjectName("text_edit_3")
            text_edit_3.setFrameShape(QtWidgets.QFrame.Panel)
            text_edit_3.setFrameShadow(QtWidgets.QFrame.Raised)

            # Set font for text_edit_3
            font_text_edit_3 = QtGui.QFont()
            font_text_edit_3.setFamily("MS Shell Dlg 2")
            font_text_edit_3.setPointSize(11)  # Adjust the point size as needed
            text_edit_3.setFont(font_text_edit_3)

            # Create a new frame for input text (frame 4)
            input_frame_4 = QtWidgets.QFrame(new_frame)
            input_frame_4.setGeometry(QtCore.QRect(600, 300, 600, 200))  # Adjust the position and size as needed
            input_frame_4.setFrameShape(QtWidgets.QFrame.Box)
            input_frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
            input_frame_4.setObjectName("input_frame_4")

            input_widget = QtWidgets.QComboBox(new_frame)
            input_widget.setEditable(True)
            input_widget.setGeometry(QtCore.QRect(450, 150, 150, 30))
            input_widget.setObjectName("input_widget")

            db_connection = connect_to_database()
            options = fetch_options_from_database(db_connection)

            for option in options:
                input_widget.addItem(option)

            if options:
                input_widget.setCurrentText(option)

            # Create a new QTextEdit for the new input field without a frame
            new_text_edit = QtWidgets.QTextEdit(new_frame)
            new_text_edit.setGeometry(QtCore.QRect(450, 100, 150, 50))  # Set the geometry as specified
            new_text_edit.setPlainText("New Text Here")  # Set the initial text (you can change this)
            new_text_edit.setObjectName("new_text_edit")  # Give it a unique object name

            # Remove the frame for the new QTextEdit
            new_text_edit.setFrameShape(QtWidgets.QFrame.NoFrame)

            # Create a QTextEdit for input text 4
            text_edit_4 = QtWidgets.QTextEdit(input_frame_4)
            text_edit_4.setGeometry(QtCore.QRect(10, 10, 580, 100))  # Adjust the position and size
            text_edit_4.setPlainText("Your Text Here 4")  # Set the initial text
            text_edit_4.setObjectName("text_edit_4")
            text_edit_4.setFrameShape(QtWidgets.QFrame.Panel)
            text_edit_4.setFrameShadow(QtWidgets.QFrame.Raised)
            # Set a frame shadow for text_edit2
            text_edit2.setFrameShape(QtWidgets.QFrame.Panel)
            text_edit2.setFrameShadow(QtWidgets.QFrame.Raised)

            # Set font for text_edit_4
            font_text_edit_4 = QtGui.QFont()
            font_text_edit_4.setFamily("MS Shell Dlg 2")
            font_text_edit_4.setPointSize(11)  # Adjust the point size as needed
            text_edit_4.setFont(font_text_edit_4)

            # Add a small QTextEdit to the new frame (top-right side of text_edit2)
            small_text_edit = QtWidgets.QTextEdit(new_frame)
            small_text_edit.setGeometry(
                QtCore.QRect(text_edit2.x() + text_edit2.width() - 104, text_edit2.y(), 104, 51))
            small_text_edit.setPlainText("Small Text")
            small_text_edit.setObjectName("small_text_edit")

            # Set font for small_text_edit
            font_small_text_edit = QtGui.QFont()
            font_small_text_edit.setFamily("MS Shell Dlg 2")
            font_small_text_edit.setPointSize(12)  # Adjust the point size as needed
            font_small_text_edit.setBold(True)  # Make the font bold
            small_text_edit.setFont(font_small_text_edit)

            # Create a "Clear" button for clearing the frame
            clear_button = QPushButton("Clear", new_frame)
            clear_button.setGeometry(QtCore.QRect(450, 60, 150, 30))  # Adjust the button position and size

            upload_button.clicked.connect(lambda: self.open_image_dialog(image_label))
            # Connect the "Clear" button to the function for clearing the frame
            clear_button.clicked.connect(lambda: self.clear_frame(new_frame, attractions_id, deals_id))
            # Optionally, configure the QLabel as needed.
            image_label.setScaledContents(True)
            image_label.setAlignment(QtCore.Qt.AlignCenter)
            # Set a frame shadow for the small_text_edit (raised shadow)
            small_text_edit.setFrameShape(QtWidgets.QFrame.Panel)
            small_text_edit.setFrameShadow(QtWidgets.QFrame.Raised)
            # Connect the save button to the save function
            self.save_attraction_button.clicked.connect(
                lambda: self.save_attractions_data_from_frame_to_database(new_frame))

            # Connect the "ADD" button to the function

        self.add_attraction_button.clicked.connect(add_new_frame)
        self.add_deals_button.clicked.connect(self.add_new_frame_to_dealspage)


import resource_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
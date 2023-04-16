import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Menu;
import javafx.scene.control.MenuBar;
import javafx.scene.control.MenuItem;
import javafx.scene.control.TextArea;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage; 

public class Main extends Application {

    public static void main(String[] args) {
        launch(args); 
    }

    @Override
    public void start(Stage arg0) throws Exception {
        BorderPane borderPane; 
        // create the border pane 
        {
            borderPane = new BorderPane(); 
        }
        // create the text area 
        {
            TextArea textArea = new TextArea();
            textArea.setPrefRowCount(10);
            textArea.setPrefColumnCount(10);
            textArea.setWrapText(true);
            textArea.setEditable(true);
            textArea.setPromptText("Enter text here");
            borderPane.setCenter(textArea); 
        }
        // create the menu bar 
        {
            MenuBar menuBar = new MenuBar(); 
            
            // set the close button 
            {
                // Menu close = new Menu("Close"); 
                // close.setOnAction(e -> {
                //     System.out.println("Closing the application");
                //     arg0.close(); 
                // }); 
                // close.setDisable(false);
                // menuBar.getMenus().add(close); 
                MenuItem close = new MenuItem("Close"); 
                close.setOnAction(e -> {
                    arg0.close(); 
                }); 
                Menu file = new Menu("File"); 
                file.getItems().add(close); 
                menuBar.getMenus().add(file); 
            }

            borderPane.setTop(menuBar); 
        } 

        // create the scene 
        {
            Scene scene = new Scene(borderPane, 500, 500); 
            arg0.setScene(scene); 
            arg0.show(); 
        } 

    } 
    
}
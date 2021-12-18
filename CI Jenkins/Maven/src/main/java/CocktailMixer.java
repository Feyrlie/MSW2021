import java.awt.Component;
import java.awt.Dimension;
import javax.swing.BoxLayout;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

/**
 * GUI for Cocktailmixer.
 * @author Tina Koppermann
 * @version 1.0 16 November 2015
 *
 */
public class CocktailMixer {
	
    /**
     * Method for graphic user interface initialization (GUI).
     */
    private void initGUI() {
        JFrame neuerMixer = new JFrame();
        // Set windows size
        neuerMixer.setSize(new Dimension(600, 400));
        // Set windows title
        neuerMixer.setTitle("Mein CocktailMixer");
        // Set windows position centered
        neuerMixer.setLocationRelativeTo(null);
        // Close application when closing window
        neuerMixer.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Generation and view of startpanel
        JPanel start = erzeugeBegruessungsPanel();
        // Add Panel to window
        neuerMixer.getContentPane().add(start); 
        // Set window to visible
        neuerMixer.setVisible(true);
    }

	private JPanel erzeugeBegruessungsPanel() {
		// TODO Auto-generated method stub
		return null;
	}    
	
	 /**
     * Main-method.
     * 
     * @param args
     *            args0
     * @throws InterruptedException
     *             InterruptedException
     * 
     */
    public static void main(String[] args) throws InterruptedException {
    	
    }
	
	

}

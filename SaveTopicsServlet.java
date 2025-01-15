import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/saveTopics")
public class SaveTopicsServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String[] topics = request.getParameterValues("topics[]");

        String url = "jdbc:mysql://localhost:3306/your_database_name"; // Update with your DB details
        String user = "your_username"; // Update with your DB username
        String password = "your_password"; // Update with your DB password

        response.setContentType("text/plain");
        PrintWriter out = response.getWriter();

        try (Connection conn = DriverManager.getConnection(url, user, password)) {
            String sql = "INSERT INTO topics (topic_name, is_checked) VALUES (?, TRUE)";
            try (PreparedStatement stmt = conn.prepareStatement(sql)) {
                if (topics != null) {
                    for (String topic : topics) {
                        stmt.setString(1, topic);
                        stmt.executeUpdate();
                    }
                    out.println("Topics saved successfully.");
                } else {
                    out.println("No topics selected.");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
            response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "Database error");
        }
    }
}

library(shiny)

row <- function(...) {
  tags$div(class = "row", ...)
}

col <- function(width, ...) {
  tags$div(class=paste0("span", width), ...)
}

ui <- shinyUI(bootstrapPage(
  
  headerPanel("File QA"),
  
  mainPanel(
    
    tags$div(
      class = "container",
      
      row(
        col(3, textInput("pdfurl", "PDF URL"))
      ),
      row(
        col(6, htmlOutput('pdfviewer')),
        # select an arbitrary .pdf 
        col(0, tags$iframe(style =
                             "height:300px; width:100%", 
                           src = 
                             "https://www.documentcloud.org/documents/4418801-nypd-cases-284.pdf"))
      )
    )
  )
))

server <- shinyServer(function(input, output, session) {
  
  output$pdfviewer <- renderText({
    #return(paste('<iframe style="height:600px; width:100%" src="', input$pdfurl, '"></iframe>', sep = ""))
  })
  
})

shinyApp(ui = ui, server = server)

# to do: 
# - add .txt file comparison 
# - add persistent data storage for crowdsourced QA responses


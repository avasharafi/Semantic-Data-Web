# Semantic-Data-Web

# dependencies: 

- dash-core-components
- dash-html-components
- pip install ipynb
- pip install dash-bootstrap-components

# File Structure: 
- Main files : MainApp.ipynb to build jupyter dash app
	     DashBoardNew.ipynb to call all subfiles and run server

- Layout files : Layout.ipynb contains main app.layout
	       Tabs.ipynb contains layout of different tabs

- Utility files: HelperFunctions.ipynb contains code uploading file, reading sample query file and initialization of tables

- Querying: QueryTextUpdates.ipynb to update query and query endpoint textbox according to user selection
	  QueryOnlineEndpoint.ipynb contains code for querying online endpoint through sparqlwrapper
	  QueryResultCallbacks.ipynb contains code for updating results after user submits a query

- Table: TableCallbacks.ipynb to update the table after query result has been updated

- Charts: ChartsResultCallback.ipynb to update the chart after query result has been updated
 	GenerateCharts.ipynb contains code for drawing the figure after query result has been updated (Called by ChartsResultCallback.ipynb)

- Statistics: Statistics.ipynb contains code for updating statistics on dashboard after query result has been updated

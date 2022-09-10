//import data from data js
const tableData = data;
console.log(data)

//reference the HTML table using d3
var tbody =d3.select("tbody");

function buildTable(data){
    //step 1: clear out previous data
    tbody.html("");  
//use fat arrow loop to loop through each object & append row and cells for each val in row
data.forEach((dataRow) =>{
    //append row to table body
    let row = tbody.append("tr");
//loop through and add value as table cell
    Object.values(dataRow).forEach((val) => {
        console.log(dataRow);
    let cell = row.append("td");
    cell.text(val);
    }
    );
});
};

function handleClick() {
    let date = d3.select("#Year").property("value"); 
    let filteredData = tableData;
  
  //filter data by date
  if (date){
      //apply filter to table data only, where datetime matches filter value
      filteredData = filteredData.filter(row => row.Year === date);
  };
  
  //rebuild table using the filtered data
  //@note: if no data was entered then filteredData will use tableData
  buildTable(filteredData);
  };
  d3.selectAll("#filter-btn").on("click", handleClick);
  
  
  //build the table when the page loads
  buildTable(tableData)
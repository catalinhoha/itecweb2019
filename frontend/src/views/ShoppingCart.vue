<template>
  <div class="shopping-cart m-xl">
    <div class="m-b-xl">
      <b-table bordered="true" :data="data">
        <template slot-scope="props">
          <b-table-column field="name" label="Nume produs">{{props.row.name}}</b-table-column>
          <b-table-column field="category" label="Categorie">{{props.row.category}}</b-table-column>
          <b-table-column
            width="200"
            field="subcategory"
            label="Subcategorie"
          >{{props.row.subcategory}}</b-table-column>
          <b-table-column field="u_m" label="U.M.">{{props.row.u_m}}</b-table-column>
          <b-table-column field="cantity" label="Cantitate" width="150">
            <b-field>
              <b-numberinput controls-position="compact" min="0" v-model="number"></b-numberinput>
            </b-field>
          </b-table-column>
          <b-table-column centered field="price" label="Pret">{{props.row.price}}</b-table-column>
        </template>
      </b-table>
    </div>
    <h2 class="level-right">Total de plata: 5.823 Lei</h2>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: [
        {
          name: "Rosii roz",
          category: "Legume",
          subcategory: "Rosii",
          u_m: "KG",
          cantity: "107",
          price: "5 Lei"
        },
        {
          name: "Cartofi albi",
          category: "Legume",
          subcategory: "Cartofi",
          u_m: "KG",
          cantity: "513",
          price: "1.5 Lei"
        },
        {
          name: "Rosii cherry",
          category: "Legume",
          subcategory: "Rosii",
          u_m: "KG",
          cantity: "55",
          price: "9 Lei"
        },
        {
          name: "Ardei Kapia",
          category: "Legume",
          subcategory: "Ardei",
          u_m: "KG",
          cantity: "89",
          price: "6 Lei"
        },
        {
          name: "Telina",
          category: "Legume",
          subcategory: "Telina",
          u_m: "Buc",
          cantity: "40",
          price: "3 Lei"
        }
      ],
      columns: [
        {
          field: "id",
          label: "ID",
          width: "40",
          numeric: true
        },
        {
          field: "first_name",
          label: "First Name"
        },
        {
          field: "last_name",
          label: "Last Name"
        },
        {
          field: "date",
          label: "Date",
          centered: true
        },
        {
          field: "gender",
          label: "Gender"
        }
      ]
    };
  }
};
</script>

<style lang="scss" scoped>
h2 {
  font-size: 1.3rem;
  font-weight: 700;
}
</style>
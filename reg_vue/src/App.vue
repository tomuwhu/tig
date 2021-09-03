<template>
  <div id="app" >
    <table class="t1">
    <th>
    <h2>
      SZTIG géptermi regisztrációs lap
    </h2>
    <table class="t2">
      <tr>
        <td class="label">
          Sztig-es emailcím
        </td>
        <td>
          <div v-if="o.saved">{{o.gmail_tig}}</div>
          <input v-else type="text" v-model="o.gmail_tig">
        </td>
      </tr>
      <tr>
        <td class="label">
          Vezetéknév
        </td>
        <td>
          <div v-if="o.saved">{{o.v_name}}</div>
          <input v-else type="text" v-model="o.v_name">
        </td>
      </tr>
      <tr>
        <td class="label">
          Keresztnév
        </td>
        <td>
          <div v-if="o.saved">{{o.k_name}}</div>
          <input v-else type="text" v-model="o.k_name">
        </td>
      </tr>
      <tr>
        <td class="label">
          Osztály/csoport
        </td>
        <td>
          <div v-if="o.saved">{{o.oszt}}</div>
          <select v-else name="s1" id="s1" v-model="o.oszt">
            <option value="-"> </option>
            <option value="9a (a)">9a - angol</option>
            <option value="9a (n)">9a - német</option>
            <option value="9c (k)">9c - kezdő</option>
            <option value="9c (h)">9c - haladó</option>
            <option value="10b (1)">10b - 1. csoport</option>
            <option value="10b (2)">10b - 2. csoport</option>
            <option value="10e (o)">10e - olasz</option>
            <option value="10e (s)">10e - spanyol</option>
          </select>
        </td>
      </tr>
      <tr>
        <td class="label w">
          Saját gmail
        </td>
        <td>
          <div v-if="o.saved">{{o.gmail_own}}</div>
          <input v-else type="text" v-model="o.gmail_own">
        </td>
      </tr>
      <tr>
        <td class="label w">
          Kedvenc állat
        </td>
        <td>
          <div v-if="o.saved">{{o.kedvenca}}</div>
          <input v-else type="text" v-model="o.kedvenca">
        </td>
      </tr>
      <tr>
        <td class="label">
          Belső hálózati jelszó &nbsp; 
        </td>
        <td>
          <div v-if="o.saved" class="r "> ---beállítva--- </div>
          <input v-else type="password" v-model="o.pw">
        </td>
      </tr>
      <tr v-if="(o.gmail_tig+'').includes('@') && o.pw.length > 5 && o.v_name.length > 2 && o.k_name.length > 2 && o.oszt">
        <td>
          <div v-if="o.saved" @click="f">Adatok</div>
        </td>
        <td>
          <div v-if="o.saved" @click="f">sikeresen beküldve</div>
          <button v-else @click="f">Beküld</button>
        </td>
      </tr>
      <tr v-if="err">
        <td colspan=2 class="r">{{err}}</td>
      </tr>
    </table>
    </th>
    </table>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'TigReg',
  data() {
    return{
      err: '',
      o: { 
        saved: false,
        pw: '',
        v_name: '',
        k_name: '',
        oszt: ''
      }
    }
  },
  methods: {
    f() {
      this.x++
      this.axios
          .post(
              'https://inf.u-szeged.hu/~tnemeth/tig_server.php',
              { 
                  p:'insert', 
                  data: {
                      gmail_tig:    this.o.gmail_tig,
                      v_name:       this.o.v_name,
                      k_name:       this.o.k_name,
                      oszt:         this.o.oszt, 
                      gmail_own:    this.o.gmail_own,
                      pw:           this.o.pw,
                      kedvenca:     this.o.kedvenca,
                      date:         Date.now()
                  } 
              }
          )
          .then( v => {
              if (v.data.gmail_tig) {
                this.o.saved = true
                console.log('Mentve');
                this.err=''
              } else this.err='Ezzel a Sztig-es emailcímmel már regisztráltak!' ;
          } )
          .catch( err => 
              console.log(err)
          )
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  user-select: none;
  text-align: center;
}
table.t2 {
  margin:2px auto;
  padding: 16px;
  background-color: rgb(211, 189, 162);
  box-shadow: 1px 1px 5px black ;
  border-radius: 7px;
}
table.t1 {
  margin:2px auto;
  padding: 16px;
  background-color: rgb(240, 227, 212);
  box-shadow: 1px 1px 5px black ;
  border-radius: 7px;
}
td {
  text-align: left;
}
td.label {
  border-bottom: solid 1px #7c94ac;
}
input {
  width: 200px;
}
select {
  width: 208px;
  text-align-last:right;
  padding-right: 29px;
  direction: rtl;
}
option {
  text-align: center;
}
button {
  padding: 7px;
  border-radius: 7px;
  text-shadow: 1px 1px 2px rgb(9, 31, 45);
  color: rgb(35, 60, 70);
}
div.r {
  color: red;
}
td.label {
  color:#2c3e50;
  font-weight: 400;
  text-shadow: 1px 1px 2px rgb(50, 48, 48);
}
td.w {
  color:#3d566f;
  font-weight: 400;
  text-shadow: 1px 1px 2px rgb(108, 102, 102);
}
td.r {
  text-align: center;
  color: red;
  background: #b4cbe3;
  margin: 5px;
  padding: 6px;
  box-shadow: 1px 1px 3px black;
  border-radius: 5px;
  text-shadow: 1px 1px 2px gray;
}
h2 {
  text-shadow: 1px 1px 2px gray;
  color: rgb(77, 40, 40);
  margin: 0px;
  padding: 6px;
  margin-bottom: 12px;
}
</style>

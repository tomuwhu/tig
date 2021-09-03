<template>
  <div id="app" >
    <h2>
      TIG belső hálózati adatlap
    </h2>
    <table>
      <tr>
        <td class="label">
          TIG-es gmail
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
          Csoport
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
        <td class="label">
          Saját gmail
        </td>
        <td>
          <div v-if="o.saved">{{o.gmail_own}}</div>
          <input v-else type="text" v-model="o.gmail_own">
        </td>
      </tr>
      <tr>
        <td class="label">
          Belső hálózati jelszó
        </td>
        <td>
          <div v-if="o.saved" class="r "> ---beállítva--- </div>
          <input v-else type="password" v-model="o.pw">
        </td>
      </tr>
      <tr>
        <td class="label">
          Kedvenc állat
        </td>
        <td>
          <div v-if="o.saved">{{o.kedvenca}}</div>
          <input v-else type="text" v-model="o.kedvenca">
        </td>
      </tr>
      <tr>
        <td>
          <div v-if="o.saved" @click="f">Adatok</div>
        </td>
        <td>
          <div v-if="o.saved" @click="f">sikeresen beküldve</div>
          <button v-else @click="f">Beküld</button>
        </td>
      </tr>
    </table>
    
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'TigReg',
  data() {
    return{
      o: { 
        saved: false 
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
                        console.log(v.data.gmail_tig);
                        if (v.data.gmail_tig) {
                          this.o.saved = true
                          console.log('Mentve');
                        }
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
table {
  margin:2px auto;
  padding: 16px;
  background-color: rgb(211, 189, 162);
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
}
div.r {
  color: red;
}
</style>

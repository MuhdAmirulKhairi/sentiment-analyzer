export async function get() {

   const users = [
      {id: 1, key: "0001"},
      {id: 2, key: "0002"},
      {id: 3, key: "0003"}
   ]

   return {
      status: 200,
      body: { users }
   }
}
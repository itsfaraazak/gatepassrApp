<script>
    import prisma from "@prisma/client";


    const client = new prisma.PrismaClient();
    const abc = client.requests.findMany();
    console.log(abc)

</script>